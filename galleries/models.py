from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    gallery = models.CharField(max_length=100, choices=[('headshots', 'headshots'), ('seniors', 'seniors'), 
                                                        ('events', 'events'), ('maternity', 'maternity'), ('couples', 'couples'),
                                                        ('engagements', 'engagements'), ('weddings', 'weddings')])
    image_url = models.TextField()

    def __str__(self):
        return self.title + ' (' + self.gallery + ')'
