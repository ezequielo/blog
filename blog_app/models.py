from django.db import models
from django.utils import timezone

# post model
class Post(models.Model):
    
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    
    def __unicode__(self):
        return self.title
    

# comment model
class Comment(models.Model):
    
    fk_post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.pub_date
