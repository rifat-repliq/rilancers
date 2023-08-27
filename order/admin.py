from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer", "job", "created_at")
    list_filter = ("job__seller", "buyer")
    search_fields = ("job__title", "buyer__username")
