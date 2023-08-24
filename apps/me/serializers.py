from rest_framework import serializers
from apps.skill.serializers import SkillModelSerializer
from apps.auth_r.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "role",
            "date_of_birth",
            "phone",
            "email",
            "bio",
            "skills",
        )

        depth = 1
