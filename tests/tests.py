import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        """Настройка перед тестами"""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page(self):
        """Тест главной страницы"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask Search Application', response.data)  # Проверяем заголовок

    def test_contact_page(self):
        """Тест страницы контактов"""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.data)

    def test_search_form(self):
        """Тест отправки формы поиска"""
        response = self.client.post('/search', data={'query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Results', response.data)

    def test_protected_page(self):
        """Тест доступа к защищенной странице (если есть авторизация)"""
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)  # Ожидаем редирект на страницу входа

if __name__ == '__main__':
    unittest.main()
