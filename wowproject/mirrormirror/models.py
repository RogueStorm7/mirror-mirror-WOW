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


class Resource(models.Model):
#     # Django automatically creates an ID column on our tables unless we tell it otherwise
    title = models.CharField(max_length=100, default=False)
    # image_url = models.URLField()
    description = models.CharField(max_length=100, default=True)
    # ingredients = models.CharField(max_length=250)
    # time = models.IntegerField()
    category_tags = models.ManyToManyField(Category)

    resource_name = models.CharField(max_length=150, default=False)
    resource_address = models.CharField(max_length=150, default=False)
    resource_zip = models.CharField(max_length=10, default=False)
    resource_phone = models.CharField(max_length=150, default=False)
    resource_url = models.URLField(max_length=150,default=True)
    resource_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.description.upper}'


# class UserNameTag(models.Model):
#     # unique=True will stop multiple tags from being created with the same name
#     tagusername = models.CharField(max_length=200, default="Anonymous")

# class Resource(models.Model):
#     # Django automatically creates an ID column on our tables unless we tell it otherwise
#     niche_tags = models.ManyToManyField(NicheTag)
#     username_tags = models.ManyToManyField(UserNameTag)
#     resource_name = models.CharField(max_length=150, help_text="Name", default=True)
#     resource_address = models.CharField(max_length=150, help_text="Address", default=True)
#     resource_zip = models.CharField(max_length=10, help_text="Zip code 00000-0000", default=True)
#     resource_phone = models.CharField(max_length=150, help_text="Phone 000-000-0000", default=True)
#     resource_url = models.CharField(max_length=150, help_text="URL", default=True)
#     resource_date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.resource_name

# class ResourceReview(models.Model):
#     username_tags = models.ManyToManyField(UserNameTag)
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     resourcereview_comment = models.TextField(max_length=4000)
#     resourcereview_date = models.DateTimeField(auto_now_add=True)
#     rate_choices = (
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#         (5,5)
#     )
#     resource_stars = models.IntegerField(choices=rate_choices)

#     def __str__(self):
#         return self.resource.resource_name
    

# class WebsiteReview(models.Model):
#     username_tags = models.ManyToManyField(UserNameTag)
#     website_review_comment = models.TextField(max_length=4000)
#     website_review_date = models.DateTimeField(auto_now_add=True)
#     rate_choices = (
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#         (5,5)
#     )
#     resource_stars = models.IntegerField(choices=rate_choices)
