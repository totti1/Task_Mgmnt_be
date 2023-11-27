from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Users(AbstractUser):
    fullname = models.CharField(max_length=60, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    class Meta:
        db_table = "authentication_users"

    def __str__(self):
        return str(self.email)


    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser