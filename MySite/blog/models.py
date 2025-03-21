from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

#Custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
        .filter(status=Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250) #varchar
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')  #CEO
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()                #text
    publish = models.DateTimeField(default=timezone.now) #datetime
    created_at = models.DateTimeField(auto_now_add=True) #datetime
    updated_at = models.DateTimeField(auto_now=True) #datetime
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    #managers
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
    #URl canonica, cada post tiene una url unica
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])