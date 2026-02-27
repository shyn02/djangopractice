from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser, BaseModel):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, blank=True, null=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.CharField(unique=True)
    mobile_number = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)