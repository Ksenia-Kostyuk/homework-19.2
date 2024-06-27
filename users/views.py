import secrets
import string
from random import random

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

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


class UserPasswordResetView(PasswordResetView):
    model = User
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        characters = string.ascii_letters + string.digits
        characters_list = list(characters)
        random.shuffle(characters_list)
        password = ''.join(characters_list[:10])
        user.set_password(make_password(password))
        user.set_password(password)
        user.save()

        send_mail(
            subject="Изменение пароля",
            message=f"Ваш новый пароль {user.password}",
            from_email=EMAIL_HOST_USER,
            recipient_list={user.email}
        )
        return super().form_valid(form)


def email_varification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
