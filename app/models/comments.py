import os
from django.db import models
from django.conf import settings
from app.models.users import Users
from app.models.posts import Posts

class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        app_label = 'app'