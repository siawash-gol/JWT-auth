from .views.login_views import (LoginView, LogoutView, RequestResetPasswordView,
                                CheckRequestResetPasswordView, SetNewPasswordView)
from .views.register_views import RegisterView, VerifyEmailView, ResendTokenVerifyEmailView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    # registration
    path('register/', RegisterView.as_view(), name='register'),
    path('resend-token/', ResendTokenVerifyEmailView.as_view(), name='resend-token'),
    path('email-verify/', VerifyEmailView.as_view(), name='email_verify'),
    # login
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset-request/', RequestResetPasswordView.as_view(),
         name="request-reset-email"),
    path('password-reset-check/<str:uidb64>/<str:token>/',
         CheckRequestResetPasswordView.as_view(), name='password-reset-check'),
    path('password-reset-complete', SetNewPasswordView.as_view(),
         name='password-reset-complete'),

]
