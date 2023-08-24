from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Skill
from .serializers import SkillSerializer


# Create your views here.
class SkillModelViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
