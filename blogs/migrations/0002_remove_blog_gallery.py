# Generated by Django 2.1.2 on 2018-10-18 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='gallery',
        ),
    ]