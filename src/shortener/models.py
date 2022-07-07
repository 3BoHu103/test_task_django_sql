from django.db import models
from django.contrib.auth.models import User
from hashlib import md5


class UserURL(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    host_name = models.CharField(default='localhost:8000/', max_length=6)
    full_url = models.URLField(unique=True, verbose_name='Длинная ссылка')
    hash_url = models.SlugField(verbose_name='Короткая ссылка')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ссылка пользователя'
        verbose_name_plural = 'Ссылки пользователей'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.host_name}{self.hash_url}'

    def save(self, *args, **kwargs):
        self.hash_url = md5(self.full_url.encode()).hexdigest()[:6]
        super().save(*args, **kwargs)
