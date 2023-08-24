from django.urls import path, include

urlpatterns = [
    path("auth/", include("apps.auth_r.urls")),
]
