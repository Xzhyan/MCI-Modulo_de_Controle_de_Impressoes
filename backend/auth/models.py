from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Nome de usuário é obrigatório!")
        
        user = self.model(
            username
        )

class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [
        (
            'admin', "Administrador",
            'supervisor', "Supervisor",
            'default', "Padrão",
        )
    ]

    username = models.CharField(max_length=50)
    role = models.CharField(choices=ROLE_CHOICES, default='default')
    
