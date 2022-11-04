from django.db import models
from django.contrib.auth.models import BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None, **other_fields):
		if not email:
			raise ValueError("User must have an email address")

		user = self.model(
			email=self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, **other_fields):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user