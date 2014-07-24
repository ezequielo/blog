from django.db import models
from django.utils import timezone, datetime_safe
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    def __unicode__(self):
        return self.name
    
    
class Post(models.Model):
    fk_user = models.ForeignKey(User)
    fk_cat = models.ForeignKey(Category)
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    
    def __unicode__(self):
        return self.title
    

class Comment(models.Model):
    fk_user = models.ForeignKey(User)
    fk_post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.pub_date


class Address(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pcode = models.CharField(max_length=10)
    street = models.CharField(max_length=60)
    
    
class Person(models.Model):
    fk_user = models.ForeignKey(User)
    fk_addr = models.ForeignKey(Address, blank=True)
    pic = models.BinaryField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    dob = models.DateField()
    extra_info = models.TextField(max_length=500)
    age = models.IntegerField(blank=True)
    


    
    
    