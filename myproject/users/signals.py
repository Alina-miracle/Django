from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Создан новый пользователь: {instance.username}")
