import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from django import forms
from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подстверждения вашей почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list={user.email}
        )
        return super().form_valid(form)


class UserPasswordResetView(FormView):
    model = User
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/password_reset_form.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = self._get_user_by_email(email)
        if not user:
            form.add_error('email', 'Пользователь не найден')
            return super().form_valid(form)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save(update_fields=['password'])

        user.email_user(
            subject="Изменение пароля",
            message=f"Ваш новый пароль {user.password}",
        )

        return super().form_valid(form)

    def _get_user_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            None


def email_varification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
