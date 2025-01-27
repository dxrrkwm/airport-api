from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "testpass123",
            "first_name": "Test",
            "last_name": "User"
        }
        self.url_register = reverse("user:create")
        self.url_login = reverse("user:token_obtain_pair")
        self.url_profile = reverse("user:profile")

    def test_user_registration_success(self):
        response = self.client.post(self.url_register, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(get_user_model().objects.filter(email=self.user_data["email"]).exists())

    def test_user_login_success(self):
        get_user_model().objects.create_user(**self.user_data)
        login_data = {
            "email": self.user_data["email"],
            "password": self.user_data["password"]
        }
        response = self.client.post(self.url_login, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_user_profile_update_success(self):
        user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_authenticate(user=user)
        update_data = {"first_name": "Updated"}
        response = self.client.patch(self.url_profile, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Updated")

    def test_user_registration_invalid_email(self):
        invalid_data = self.user_data.copy()
        invalid_data["email"] = "invalid-email"
        response = self.client.post(self.url_register, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_wrong_password(self):
        get_user_model().objects.create_user(**self.user_data)
        wrong_data = {
            "email": self.user_data["email"],
            "password": "wrongpass123"
        }
        response = self.client.post(self.url_login, wrong_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_profile_access(self):
        response = self.client.get(self.url_profile)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_password_minimum_length(self):
        short_pass_data = self.user_data.copy()
        short_pass_data["password"] = "short"
        response = self.client.post(self.url_register, short_pass_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_max_length(self):
        long_email_data = self.user_data.copy()
        long_email_data["email"] = "a" * 246 + "@example.com"  # 254 characters
        response = self.client.post(self.url_register, long_email_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_special_characters_in_name(self):
        special_char_data = self.user_data.copy()
        special_char_data["first_name"] = "Test@#$%"
        response = self.client.post(self.url_register, special_char_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
