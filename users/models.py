from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(_('phone number'), blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None
    
    def __str__(self):
        return self.email
    
