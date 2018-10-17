from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)