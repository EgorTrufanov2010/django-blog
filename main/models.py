from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)         # заголовок поста
    created_at = models.DateTimeField(default=timezone.now)  # дата создания
    content = models.TextField()                      # текст поста

    def __str__(self):
        return self.title
