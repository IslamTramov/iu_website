from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class custom_user(AbstractUser):
    avatar_url = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.username


class news_post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='post_images')
    author = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        tokens = (
            'News post:',
            f'\tid: {self.id}',
            f'\ttitle: {self.title}',
            f'\ttext: {self.text}',
        )
        return '\n'.join(tokens)

