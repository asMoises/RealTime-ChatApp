from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
  user = instance
  # Verifica se o usuário foi criado
  # Se sim, cria o perfil do usuário
  # Se não, não faz nada
  
  if created:
    Profile.objects.create(
      user=user
      )