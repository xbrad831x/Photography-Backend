# Generated by Django 2.1.2 on 2018-10-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
