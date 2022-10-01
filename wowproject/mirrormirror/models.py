import re
from django.db import models
import datetime

# Category model has one attribute- catname = category name
# "unique=True" will stop multiple tags from being created with the same name
class Category(models.Model):
    unique=True 
    catname = models.CharField(max_length=50)
    # Displays the category name as a string
    def __str__(self):
        return (self.catname)


# The Resource attributes are identical to the fields in the "add resource" form and each attribute can be edited/updated in the database via the form
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
    resource_date = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")
    
    # Displays the resource name and title as a string
    def __str__(self):
        return f'{self.resource_name} - {self.title}'


# Each resource review is related to an individual resource via a one-to-many relationship
class ResourceReview(models.Model):
    """Review on a Resource"""
    review = models.TextField(max_length=4000)
    user_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    stars = models.IntegerField(choices=rating)

    # Displays the resource title as a string
    def str(self):
        return self.resource.title


# Each website review is saved into the database so it may be edited/updated or deleted 
class WebsiteReview(models.Model):
    '''An ID field is automatically added to all Django models'''
    review = models.TextField(max_length=4000)
    user_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    stars = models.IntegerField(choices=rating)


# Each comment is saved into the database so it may be edited/updated or deleted
class Comment(models.Model):
    '''An ID field is automatically added to all Django models'''
    description = models.CharField(max_length=500)
    commentor_name = models.CharField(max_length=255,default="Anonymous",help_text="  ")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")
