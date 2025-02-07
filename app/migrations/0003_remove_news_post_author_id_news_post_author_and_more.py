# Generated by Django 5.1.4 on 2025-02-07 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_news_post_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_post',
            name='author_id',
        ),
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news_post',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
