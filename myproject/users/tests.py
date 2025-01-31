# users/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Order  # Если у вас есть такие модели


# Импортируйте вашу модель User, если это нужно

# Тестирование модели User
class UserModelTest(TestCase):
    def test_create_user(self):
        # Создаем нового пользователя
        user = User.objects.create(username="testuser", email="testuser@example.com")

        # Проверяем, что поля создались верно
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")


# Тестирование модели Order (с примером метода get_total)
class OrderModelTest(TestCase):
    def test_order_total(self):
        # Создаем заказ с общей суммой и скидкой
        order = Order.objects.create(total=100, discount=20)

        # Проверяем, что метод get_total() правильно рассчитывает итоговую сумму
        self.assertEqual(order.get_total(), 80)  # 100 - 20 = 80


# Тестирование представлений (views)
class UserViewsTest(TestCase):
    def test_user_list_view(self):
        # Отправляем GET-запрос на страницу списка пользователей
        response = self.client.get(reverse('user_list'))  # Замените на свой URL
        # Проверяем, что статус ответа 200
        self.assertEqual(response.status_code, 200)
        # Проверяем, что использовался правильный шаблон
        self.assertTemplateUsed(response, 'users/user_list.html')  # Замените на свой шаблон


# Тестирование прав доступа для админа и обычного пользователя
class AccessTest(TestCase):
    def test_admin_access(self):
        # Создаем суперпользователя
        admin_user = User.objects.create_superuser(username='admin', password='password')
        # Логинимся как администратор
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('admin_page'))  # Замените на свою страницу
        self.assertEqual(response.status_code, 200)

    def test_normal_user_access(self):
        # Создаем обычного пользователя
        normal_user = User.objects.create_user(username='normal', password='password')
        # Логинимся как обычный пользователь
        self.client.login(username='normal', password='password')
        response = self.client.get(reverse('admin_page'))  # Замените на свою страницу
        self.assertEqual(response.status_code, 403)  # Ожидаем статус 403, т.к. доступ только для админов
