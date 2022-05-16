from django.db.utils import IntegrityError
from django import forms

from mirrormirror.models import *


class CommentForm(forms.ModelForm):
    commentor_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    
    
    class Meta:
        model = Comment
        fields = ['commentor_name','description']  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form
        # fields = ['description']

    # *args: list of arguments (single * is for lists, python syntax)
    # **kwargs = dictionary key word arguments (double ** is for dictionaries, python syntax)
    def __init__(self, *args, **kwargs):
        # Run the __init__ method of the class that this one inherits from (forms.ModelForm)
        # Fun fact-- this works for any method of any class being inherited!
        super().__init__(*args, **kwargs)

        self.fields['commentor_name'].label = 'Your Name:'
        self.fields['description'].label = 'Your Comment:'





# class ResourceReviewForm(forms.ModelForm):
#     class Meta:
#         model = ResourceReview
#         fields = ["resource_stars","resourcereview_comment"]

# class NicheTagForm(forms.ModelForm):
#     class Meta:
#         model = NicheTag
#         fields = ['tagnichename']

#     def __init__(self, *args, **kwargs):
#         # We send the form the keyword 'task', so we can pop that out now to use
#         self.task = kwargs.pop('task', None)
#         super().__init__(*args, **kwargs)

#         # Every ModelForm has a self.instance, the instance of its model that we're 
#         # editing, deleting, etc
#         self.instance.resource = self.resource
#         self.fields['nichename'].label = 'Category'

#     def save(self, *args, **kwargs):
#         # Usually, calling <form>.save() will try to create a new instance of the model.
#         # In this case, a tag with the given name might already exist. Use get_or_create()
#         # to only create one if it does not already exist

#         # Alternative Django 
#         # tag, _ = Tag.objects.get_or_create(name=self.data['name'])

#         try:
#             tag = NicheTag.objects.create(name=self.data['tagnichename'])
#         except IntegrityError:
#             tag = NicheTag.objects.get(name=self.data['tagnichename'])

#         # Automatically add this tag to the task, whether it is new or not
#         self.resource.tags.add(tag)