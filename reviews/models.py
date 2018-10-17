from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to= 'review_pic/')
    created_at = models.DateTimeField(auto_now_add=True)