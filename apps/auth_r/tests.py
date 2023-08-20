from rest_framework.test import APITestCase
from rest_framework import status
from apps.auth_r.models import User


class UserRegistrationAPITestCase(APITestCase):
    def test_user_registration(self):
        url = "/api/v1/auth/register"  # Update this URL if needed
        data = {
            "phone": "+8801784254902",
            "email": "test@example.com",
            "password": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().phone, "+8801784254902")
