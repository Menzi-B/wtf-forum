from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)  # foreignkey associates author with User

    def __str__(self):
        return self.title

    # defining a model method a.k.a a function within the table structure definition
    def snippet(self):
        return self.body[:50] + '...'  # just specifying [start:end], no need to specify 0 as python understands
        # internally empty stands for zero

