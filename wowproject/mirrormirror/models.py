import re
from django.db import models
import datetime

class Comment(models.Model):
    '''An ID field is automatically added to all Django models'''
    description = models.CharField(max_length=255)
    commentor_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")

class Category(models.Model):
    # unique=True will stop multiple tags from being created with the same name
    catname = models.CharField(max_length=50)
    def __str__(self):
        return (self.catname)

class Resource(models.Model):
#     # Django automatically creates an ID column on our tables unless we tell it otherwise
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


class ResourceReview(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    resourcereview_username = models.TextField(max_length=4000)
    resourcereview_comment = models.TextField(max_length=4000)
    resourcereview_date = models.DateTimeField(auto_now_add=True)
    resourcereview_rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    resourcereview_stars = models.IntegerField(choices=resourcereview_rating)

    def __str__(self):
        return self.resource.resource_name
