# Generated by Django 2.1.2 on 2018-10-17 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
    ]