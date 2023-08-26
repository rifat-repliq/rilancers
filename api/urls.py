from django.urls import path, include

urlpatterns = [
    path("auth/", include("auth_r.urls")),
    path("skills/", include("skill.urls")),
    path("me/", include("me.urls")),
]
