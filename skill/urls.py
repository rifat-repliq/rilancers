from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillModelViewSet

router = DefaultRouter()
router.register(r"", SkillModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
