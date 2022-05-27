# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import TemplateView, ListView
from mirrormirror.forms import *
from mirrormirror.models import *
from django.db.models import Q
  

# Create your views here.
class HomeView(TemplateView):
    template_name='home.html'


class WelcomeView(TemplateView):
    template_name='welcome.html'


class AceQuizView(View):
    def get(self, request):
        return render(
            request=request,
            # render ace-quiz.html page
            template_name='ace-quiz.html',
        )


class ScoreStatsView(TemplateView):
    template_name='score_stats.html'


class ResourcesView(View):
    def get(self, request):
        return render(
            request=request,
            # render resources.html page
            template_name='resources.html',
        )


class MentalHealthView(View):
    def get(self, request):
        resources_present = Resource.objects.exists()
        resources = Resource.objects.filter(category_tags='2').values()
        context = {
        'resources_present': resources_present,
        'resources': resources,
        }
        return render(request, 'mentalhealth.html', context)

class JusticeImpactedView(View):
    def get(self, request):
        resources_present = Resource.objects.exists()
        resources = Resource.objects.filter(category_tags='3').values()
        context = {
        'resources_present': resources_present,
        'resources': resources,
        }
        return render(request, 'justiceimpacted.html', context)

class PhysicalHealthView(View):
    def get(self, request):
        resources_present = Resource.objects.exists()
        resources = Resource.objects.filter(category_tags='4').values()
        context = {
        'resources_present': resources_present,
        'resources': resources,
        }
        return render(request, 'physicalhealth.html', context)

class OverallWellnessView(View):
    def get(self, request):
        resources_present = Resource.objects.exists()
        resources = Resource.objects.filter(category_tags='5').values()
        context = {
        'resources_present': resources_present,
        'resources': resources,
        }
        return render(request, 'overallwellness.html', context)
        
class NationalResourcesView(View):
    def get(self, request):
        resources_present = Resource.objects.exists()
        resources = Resource.objects.filter(category_tags='6').values()
        context = {
        'resources_present': resources_present,
        'resources': resources,
        }
        return render(request, 'nationalresources.html', context)

class ZipcodeView(TemplateView):
    template_name = 'zipcode.html'

class ZipResultsView(ListView):
    model = Resource
    template_name = 'zipcode.html'

    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = Resource.objects.filter(
            Q(resource_zip__icontains=query) 
        )
        return object_list


# Code for admin pages to create, view, edit, and delete resources
def index(request):
    resources_present = Resource.objects.exists()
    resources = Resource.objects.all()
    context = {
        'resources_present': resources_present,
        'resources': resources,
    }
    return render(request, 'resourcetemppage.html', context)

def resource_create(request):
    if request.method == 'GET':
        context = {
            'form': ResourceForm(),
        }
        return render(request, 'resourcecreate.html', context)
    else:
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('resourcetemppage')
        context = {
            'form': form,
        }
        return render(request, 'resourcecreate.html', context)
 
def resource_edit(request, pk):
    resource = Resource.objects.get(pk=pk)
 
    if request.method == 'GET':
        context = {
            'resource': resource,
            'form': ResourceForm(instance=resource)
        }
        return render(request, 'resourceedit.html', context)
    else:
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resourcetemppage')
 
        context = {
            'resource': resource,
            'form': form,
        }
        return render(request, 'resourceedit.html', context)
 
def resource_delete(request, pk):
    resource = Resource.objects.get(pk=pk)
 
    if request.method == 'GET':
        context = {
            'resource': resource,
            'form': DeleteResourceForm(instance=resource)
        }
 
        return render(request, 'resourceedit.html', context)
    else:
        resource.delete()
        return redirect('resourcetemppage')    


# Resource categories
class CategoryListView(View):
    def get(self, request):
        categorys = Category.objects.all().order_by('-id')
        form = CategoryForm()

        return render(
            request=request, template_name = 'categorycreate.html', context = {'categorys': categorys, 'form': form}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new comment in the list'''
        form=CategoryForm(request.POST)
        if form.is_valid():
            category_catname = form.cleaned_data['catname']
            Category.objects.create(catname=category_catname)

        # "redirect" to the comment page
        return redirect('category_list')


class CategoryDetailView(View):
    def get(self, request, category_id):
        '''...'''
        category = Category.objects.get(id=category_id)
        form = CategoryForm(initial={'catname': category.catname})
        
        return render(
            request=request, template_name='categoryupdate.html', context={'form':form, 'id': category_id})
    def post(self, request, category_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        category = Category.objects.filter(id=category_id)
        if 'save' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                category_catname = form.cleaned_data['catname']
                category.update(catname=category_catname)
                category.update

        elif 'delete' in request.POST:
            category.delete()

        # "redirect" to the list page
        return redirect('category_list')


# gets & posts Website Reviews + Comments; displays them in designated divs via templating on same html page
def get_and_post(request):
    if request.method == 'GET':
        resource_reviews = ResourceReview.objects.all().order_by('-id')
        site_reviews = WebsiteReview.objects.all().order_by('-id')
        comments = Comment.objects.all().order_by('-id')
        resource_review_form = ResourceReviewForm()
        website_review_form = WebsiteReviewForm()
        comment_form = CommentForm()

        context = {
            'resource_reviews': resource_reviews,
            'resource_review_form': resource_review_form,
            'site_reviews': site_reviews, 
            'website_review_form': website_review_form,
            'comments': comments, 
            'comment_form': comment_form,
        }
        return render(request, 'reviews_comments.html', context)
    resource_review_form = ResourceReviewForm()
    website_review_form = WebsiteReviewForm()
    comment_form = CommentForm()
    if request.method == 'POST':
        if 'widget1' in request.POST:
            resource_review_form = ResourceReviewForm(request.POST)
            if resource_review_form.is_valid():
                resourcereview_review = resource_review_form.cleaned_data['review']
                resourcereview_user_name = resource_review_form.cleaned_data['user_name']
                resourcereview_stars = resource_review_form.cleaned_data['stars']
                resourcereview_resource = resource_review_form.cleaned_data['resource']
                ResourceReview.objects.create(review=resourcereview_review, user_name=resourcereview_user_name, stars=resourcereview_stars, resource=resourcereview_resource)
                return redirect('display')
        if 'widget2' in request.POST:
            website_review_form = WebsiteReviewForm(request.POST)
            if website_review_form.is_valid():
                websitereview_review = website_review_form.cleaned_data['review']
                websitereview_user_name = website_review_form.cleaned_data['user_name']
                website_review_stars = website_review_form.cleaned_data['stars']
                WebsiteReview.objects.create(review=websitereview_review, user_name=websitereview_user_name, stars=website_review_stars)
                return redirect('display')
        if 'widget3' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_description = comment_form.cleaned_data['description']
                comment_commentor_name = comment_form.cleaned_data['commentor_name']
                Comment.objects.create(description=comment_description, commentor_name=comment_commentor_name)
                return redirect('display')
    context = {
            'resource_reviews': resource_reviews,
            'resource_review_form': resource_review_form,
            'site_reviews': site_reviews, 
            'website_review_form': website_review_form,
            'comments': comments, 
            'comment_form': comment_form,
        }
    return render(request, 'reviews_comments.html', context=context)



class ResourceReviewDetailView(View):
    def get(self, request, review_id):
        '''GET the detail view of the Comment to modify it'''
        review = ResourceReview.objects.get(id=review_id)
        form = ResourceReviewForm(initial={'review': review.review, 'user_name': review.user_name, 'stars': review.stars, 'resource': review.resource})
        
        return render(
            request=request, template_name='resourcereview_update.html', context={'form':form, 'id': review_id})

    def post(self, request, review_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        review = ResourceReview.objects.filter(id=review_id)
        if 'save' in request.POST:
            form = ResourceReviewForm(request.POST)
            if form.is_valid():
                resource_review = form.cleaned_data['review']
                user_name = form.cleaned_data['user_name']
                resource = form.cleaned_data['resource']
                stars = form.cleaned_data['stars']
                review.update(review=resource_review)
                review.update(user_name=user_name)
                review.update(resource=resource)
                review.update(stars=stars)

        elif 'delete' in request.POST:
            review.delete()

        # "redirect" to the list page
        return redirect('display')


class WebsiteReviewDetailView(View):
    def get(self, request, review_id):
        '''GET the detail view of the Comment to modify it'''
        review = WebsiteReview.objects.get(id=review_id)
        form = WebsiteReviewForm(initial={'review': review.review, 'user_name': review.user_name, 'stars': review.stars})
        
        return render(
            request=request, template_name='websitereview_update.html', context={'form':form, 'id': review_id})
    def post(self, request, review_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        review = WebsiteReview.objects.filter(id=review_id)
        if 'save' in request.POST:
            form = WebsiteReviewForm(request.POST)
            if form.is_valid():
                website_review = form.cleaned_data['review']
                user_name = form.cleaned_data['user_name']
                stars = form.cleaned_data['stars']
                review.update(review=website_review)
                review.update(user_name=user_name)
                review.update(stars=stars)

        elif 'delete' in request.POST:
            review.delete()

        # "redirect" to the list page
        return redirect('display')


class UserCommentDetailView(View):
    def get(self, request, comment_id):
        '''GET the detail view of the Comment to modify it'''
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(initial={'description': comment.description, 'commentor_name': comment.commentor_name})
        
        return render(
            request=request, template_name='review_commentsupdate.html', context={'form':form, 'id': comment_id})
    def post(self, request, comment_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        comment = Comment.objects.filter(id=comment_id)
        if 'save' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_description = form.cleaned_data['description']
                comment_commentor_name = form.cleaned_data['commentor_name']
                comment.update(description=comment_description)
                comment.update(commentor_name=comment_commentor_name)

        elif 'delete' in request.POST:
            comment.delete()

        # "redirect" to the list page
        return redirect('display')






# def rate(request, id):
#     post = Resource.objects.get(id=id)
#     form = ResourceForm(request.POST or None)
#     if form.is_valid():
#         resourcereview_username = request.POST.get('name')
#         resourcereview_stars = request.POST.get('stars')
#         resourcereview_comment = request.POST.get('comment')
#         review = ResourceReview(resourcereview_username=resourcereview_username, resourcereview_stars = resourcereview_stars,  resourcereview_comment=resourcereview_comment , resource=post)
#         review.save()
#         return redirect('index')

#     form = ResourceReviewForm()
#     context = {
#         "form":form

#     }
#     return render(request, 'resourcereview.html',context)

class ResourceReviewListView(View):
    def get(self, request):
        '''listing all user reviews in reverse order that they were created'''
        review = ResourceReview.objects.all().order_by('-id')
        form = ResourceReviewForm()

        return render(
            request=request, template_name = 'reviews_comments.html', context = {'resource_reviews': review, 'resource_review_form': form}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new comment in the list'''
        form=ResourceReviewForm(request.POST)
        if form.is_valid():
            resource_review = form.cleaned_data['resourcereview_comment']
            resource_review_username = form.cleaned_data['resourcereview_username']
            ResourceReview.objects.create(resourcereview_comment=resource_review, resourcereview_username=resource_review_username)

        # "redirect" to the comment page
        return redirect('resourcereview_list')








