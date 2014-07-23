from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    def __unicode__(self):
        return self.name
    
class Post(models.Model):
    fk_cat = models.ForeignKey(Category)
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    
    def __unicode__(self):
        return self.title
    

class Comment(models.Model):
    fk_post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.pub_date



    
    
    