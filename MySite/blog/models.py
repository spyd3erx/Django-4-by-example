from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250) #varchar
    slug = models.SlugField(max_length=250)  #CEO
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()                #text
    publish = models.DateTimeField(default=timezone.now) #datetime
    created_at = models.DateTimeField(auto_now_add=True) #datetime
    updated_at = models.DateTimeField(auto_now=True) #datetime

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title