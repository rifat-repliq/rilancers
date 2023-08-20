from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The Phone Number field must be set")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)


def generate_username_from_datetime():
    """Generate a username using the current date and timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"user_{timestamp}"


class User(AbstractUser, PermissionsMixin):
    USER_ROLE_CHOICES = [
        ("SELLER", "Seller"),
        ("BUYER", "Buyer"),
        ("ORGANIZATION", "Organization"),
    ]
    phone = PhoneNumberField(unique=True, region="BD")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default="SELLER")
    username = models.CharField(
        max_length=150,
        unique=True,
        default=generate_username_from_datetime,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return str(self.phone)
