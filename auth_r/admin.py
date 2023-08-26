from django.contrib import admin
from .models import User


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "phone",
        "username",
        "get_full_name",
        "role",
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = "Full Name"


admin.site.register(User, UserModelAdmin)
