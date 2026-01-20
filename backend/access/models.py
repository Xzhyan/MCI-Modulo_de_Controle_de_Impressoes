from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class Role(models.Model):
    role = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.role


class Function(models.Model):
    function = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.function


class Sector(models.Model):
    sector = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sector


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, access_level='default', **extra_fields):
        if not username:
            raise ValueError("O nome de usuário é obrigatório!")
        
        if not password:
            raise ValueError("O uso de uma senha é obrigatório!")
        
        user = self.model(username=username, access_level=access_level, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, access_level='admin', **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ACCESS_LEVEL = (
        ('admin', "Administrador"),
        ('supervisor', "Supervisor"),
        ('default', "Padrão"),
        ('visitor', "Visitante"),
    )

    username = models.CharField(max_length=50, unique=True)
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL)
    role_id = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    function_id = models.ForeignKey(Function, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    @property
    def is_staff(self):
        return self.is_admin