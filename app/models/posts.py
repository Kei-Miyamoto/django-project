import os
from django.db import models
from django.conf import settings
from app.models.users import Users

class Posts(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    reply_to_post_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    quote_post_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='quotes')
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
        app_label = 'app'