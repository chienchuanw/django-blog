# Generated by Django 5.0.6 on 2024-07-10 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
    ]
