from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User


    
class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = HTMLField()
    slug = AutoSlugField(populate_from="title", unique=True, null=True, default=None)   
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title