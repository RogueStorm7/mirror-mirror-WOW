import re
from django.db import models
import datetime


class Category(models.Model):
    # unique=True will stop multiple tags from being created with the same name
    catname = models.CharField(max_length=50)
    def __str__(self):
        return (self.catname)

# NEED TO FIX!!!!
class Resource(models.Model):
    # Django automatically creates an ID column on our tables unless we tell it otherwise
    title = models.CharField(max_length=100, default=False)
    description = models.CharField(max_length=100, default=True)
    category_tags = models.ManyToManyField(Category)
    resource_name = models.CharField(max_length=150, default=False)
    resource_address = models.CharField(max_length=150, default=False)
    resource_city = models.CharField(max_length=150, default=False)
    resource_state = models.CharField(max_length=20, default=False)
    resource_zip = models.CharField(max_length=10, default=False)
    resource_phone = models.CharField(max_length=150, default=False)
    resource_url = models.URLField(max_length=150,default=True)
    resource_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.date.upper}'


class Comment(models.Model):
    '''An ID field is automatically added to all Django models'''
    description = models.CharField(max_length=500)
    commentor_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")


# NEED TO FIX!!!!
class ResourceReview(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    resourcereview_username = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    resourcereview_comment = models.CharField(max_length=1000)
    resourcereview_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.resource.resource_name


class WebsiteReview(models.Model):
    '''An ID field is automatically added to all Django models'''
    review = models.CharField(max_length=500)
    user_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")