from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Post(models.Model):
    owner = models.ForeignKey(User)
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=Post)