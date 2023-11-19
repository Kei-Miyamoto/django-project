import os
from django.db import models
from django.conf import settings

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_name = models.CharField(unique=True, max_length=16)
    name = models.CharField(max_length=16)
    biography = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(unique=True, max_length=11)
    link = models.URLField(null=True, blank=True)
    icon = models.ImageField(upload_to='icon/', null=True)
    adult_flag = models.BooleanField(default=0)
    ban_count = models.IntegerField(null=True)
    status = models.IntegerField(default=0)
    hash_password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now_add=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        app_label = 'app'
        indexes = [
            models.Index(fields=['email'], name='idx_email'),
            models.Index(fields=['user_name'], name='idx_user_name'),
        ]