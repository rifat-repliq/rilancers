from django.urls import path, include
from rest_framework import routers
from .views import SkillModelViewSet

router = routers.DefaultRouter()
router.register(prefix="", viewset=SkillModelViewSet)

urlpatterns = [
    # Other URL patterns
    path("", include(router.urls)),
]
