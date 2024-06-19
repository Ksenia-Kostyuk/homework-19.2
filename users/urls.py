from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import UserCreateView, email_varification, UserPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", UserCreateView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'
    ),
    path("email-confirm/<str:token>/", email_varification, name='email-confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
