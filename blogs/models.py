from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    gallery = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
