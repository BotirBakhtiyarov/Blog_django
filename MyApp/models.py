from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name = 'comments', on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_detail', args=self.pk)

    def __str_(self):
        return self.text
