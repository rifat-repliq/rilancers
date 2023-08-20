from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(phone=phone))
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
