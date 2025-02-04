from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import User

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 10  # Количество элементов на странице

    def get_queryset(self):
        return User.objects.filter(is_active=True)  # Показываем только активных пользователей
users = CustomUser.objects.active_users()
