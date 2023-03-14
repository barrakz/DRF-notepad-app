from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)