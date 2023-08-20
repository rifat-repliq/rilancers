from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserRegistrationSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
