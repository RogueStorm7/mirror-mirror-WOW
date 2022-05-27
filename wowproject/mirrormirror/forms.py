from django.db.utils import IntegrityError
from django import forms
from mirrormirror.models import *



class DisabledForm():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        labels = {
          
        }
        fields = '__all__'


class DeleteResourceForm(ResourceForm, DisabledForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledForm.__init__(self)


class CategoryForm(forms.ModelForm):
    catname = models.CharField(max_length=50) 
    class Meta:
        model = Category
        fields = ['catname'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catname'].label = 'Category Name:'


class ResourceReviewForm(forms.ModelForm):
    widget1 = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    user_name = models.CharField(max_length=255)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    stars = models.IntegerField(choices=rating, default=1)
    class Meta:
        model = ResourceReview
        fields = ["user_name", "resource", "stars","review"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].label = 'Your Name:'
        self.fields['resource'].label = 'Resource Name:'
        self.fields['stars'].label = 'Stars:'
        self.fields['review'].label = 'Your Feedback:'



class WebsiteReviewForm(forms.ModelForm):
    widget2 = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    user_name = models.CharField(max_length=255)
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    stars = models.IntegerField(choices=rating, default=1)
    class Meta:
        model = WebsiteReview
        fields = ['user_name', 'stars','review']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].label = 'Your Name:'
        self.fields['stars'].label = 'Stars:'
        self.fields['review'].label = 'Your Feedback:'
        



class CommentForm(forms.ModelForm):
    widget3 = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    commentor_name = models.CharField(max_length=255)
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


    
