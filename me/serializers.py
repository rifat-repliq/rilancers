from rest_framework import serializers
from skill.serializers import SkillModelSerializer
from auth_r.models import User
from skill.models import Skill


class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillModelSerializer(many=True)

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

    def update(self, instance, validated_data):
        # Pop the skills list from validated_data and process it separately
        skills = validated_data.pop("skills", [])

        # Update user profile fields
        instance = super().update(instance, validated_data)

        # Update user's skills
        if skills:
            skill_titles = [skill["title"] for skill in skills]
            new_skills = Skill.objects.filter(title__in=skill_titles)
            instance.skills.set(new_skills)
        else:
            # If skills list is empty, remove all existing skills
            instance.skills.clear()

        return instance
