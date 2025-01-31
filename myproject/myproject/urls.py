from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import register
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Добавляем URL для пользователей
path('register/', register, name='register'),
path('accounts/', include('accounts.urls')),
]
