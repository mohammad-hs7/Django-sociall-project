from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='posts')
    title = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    body = models.TextField(max_length=350)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('create', 'body')

    def __str__(self):
        return f'{self.title} -- {self.user}'

    def get_absolute_url(self):
        return reverse('home:post_delete', args=self.id)

class Comments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='your_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_comment', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -- {self.body[:30]}'





