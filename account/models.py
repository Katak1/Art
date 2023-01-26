from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, fullname, password, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not fullname:
            raise ValueError('Username not filled')

        user = self.model(email=self.normalize_email(email),
                          fullname=fullname,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, fullname, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, fullname, password, **extra_fields)

    def create_superuser(self, email, fullname, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, fullname, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True,)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True, blank=True)
    date_of_birth = models.DateField(auto_now=True)
    password = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return f'{self.email} -> {self.fullname}'