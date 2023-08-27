from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Docs
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    # API's
    path("auth/", include("auth_r.urls")),
    path("me/", include("me.urls")),
    path("skills/", include("skill.urls")),
    path("categories/", include("category.urls")),
    path("jobs/", include("job.urls")),
    path("orders/", include("order.urls")),
]
