from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra_fields):
        """Creates and saves user with given phone and password"""
        if not phone_number:
            raise ValueError('phone number required!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(phone_number, password, **extra_fields)


class MyUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(
        regex=r'^(\+98|0)?9\d{9}$',
        message="Phone number must be entered in the format: '09...' or format: '+989..."
                                )
    phone_number = models.CharField(validators=[phone_regex], verbose_name='Mobile Number', unique=True,
                                    max_length=13)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

