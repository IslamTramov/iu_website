# Generated by Django 5.1.4 on 2025-02-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_news_post_author_id_news_post_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_post',
            old_name='image_url',
            new_name='image',
        ),
    ]
