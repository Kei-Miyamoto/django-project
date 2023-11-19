import os
from django.db import models
from django.conf import settings
from app.models.users import Users

class Follows(models.Model):
    follow_id = models.BigAutoField(primary_key=True)
    following = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='followings')
    follower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='followers')
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'follows'
        app_label = 'app'