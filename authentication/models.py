from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyAccountManager


# CUSTOM USER MODEL
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, primary_key=True)
    name = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=12, error_messages={
        'required': "Thiếu vai trò"
    })

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
