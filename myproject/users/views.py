from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from .models import CustomUser

class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'
