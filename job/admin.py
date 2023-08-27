from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "price", "seller")
    list_filter = ("category", "seller")
    search_fields = ("title", "seller__username")
