# Generated by Django 5.0.6 on 2024-07-06 12:50

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_options_alter_tag_options_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
