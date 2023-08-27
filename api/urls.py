from django.urls import path, include

urlpatterns = [
    path("auth/", include("auth_r.urls")),
    path("me/", include("me.urls")),
    path("skills/", include("skill.urls")),
    path("categories/", include("category.urls")),
    path("jobs/", include("job.urls")),
    path("orders/", include("order.urls")),
]
