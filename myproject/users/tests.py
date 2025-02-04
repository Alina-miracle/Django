from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser  # Если у тебя кастомная модель пользователя

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="testuser@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class UserViewsTest(TestCase):
    def test_user_list_view(self):
        response = self.client.get(reverse('user_list'))  # Убедись, что URL правильный
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')
