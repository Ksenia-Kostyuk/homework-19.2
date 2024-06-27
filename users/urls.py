from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import UserCreateView, email_varification, UserPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", UserCreateView.as_view(), name='register'),
    path("email-confirm/<str:token>/", email_varification, name='email-confirm'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
