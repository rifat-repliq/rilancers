from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegistrationView


urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("register", RegistrationView.as_view(), name="register"),
    path("refresh", TokenRefreshView.as_view(), name="refresh-token"),
    path("verify", TokenVerifyView.as_view(), name="verify-token"),
]
