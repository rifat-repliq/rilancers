from django.contrib import admin
from .models import Skill


# Register your models here.
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


admin.site.register(Skill, SkillModelAdmin)
