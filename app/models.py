from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class news_post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    text = models.TextField()
    author_id = models.UUIDField(editable=True)
    creation_date = models.DateTimeField()

    def __str__(self):
        tokens = (
            'News post:',
            f'\tid: {self.id}',
            f'\ttitle: {self.title}',
            f'\ttext: {self.text}',
        )
        return '\n'.join(tokens)


class custom_user(AbstractUser):
    avatar_url = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.username
