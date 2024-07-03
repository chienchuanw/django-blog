# Generated by Django 5.0.6 on 2024-07-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tag_remove_post_tag_alter_post_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.tag'),
        ),
    ]
