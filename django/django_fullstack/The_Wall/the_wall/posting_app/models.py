from django.db import models
from django.apps import apps
from login_app.models import Users

class messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="related_messages", on_delete = models.CASCADE)

class comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="related_comments", on_delete = models.CASCADE)
    messages = models.ForeignKey(messages, related_name="messagetocomment_relation", on_delete = models.CASCADE)

