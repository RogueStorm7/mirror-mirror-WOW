# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import TemplateView
from mirrormirror.forms import *
from mirrormirror.models import *


class UserCommentListView(View):
    def get(self, request):
        '''listing all user comments in reverse order that they were created'''
        comments = Comment.objects.all().order_by('-id')
        form = CommentForm()

        return render(
            request=request, template_name = 'reviews_comments.html', context = {'comments': comments, 'form': form}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new comment in the list'''
        form=CommentForm(request.POST)
        if form.is_valid():
            comment_description = form.cleaned_data['description']
            comment_commentor_name = form.cleaned_data['commentor_name']
            Comment.objects.create(description=comment_description, commentor_name=comment_commentor_name)

        # "redirect" to the comment page
        return redirect('comment_list')

class UserCommentDetailView(View):
    def get(self, request, comment_id):
        '''GET the detail view of a single task on the todo list'''
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(initial={'description': comment.description, 'commentor_name': comment.commentor_name})
        
        return render(
            request=request, template_name='commentupdate.html', context={'form':form, 'id': comment_id})
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
        return redirect('comment_list')



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
            template_name='ace-quiz.html',)

class ScoreStatsView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='score_stats.html', 

        )



def index(request):
    resources_present = Resource.objects.exists()
    resources = Resource.objects.all()
    context = {
        'resources_present': resources_present,
        'resources': resources,
    }
    return render(request, 'index.html', context)

def resource_create(request):
    if request.method == 'GET':
        context = {
            'form': ResourceForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
 
 
def resource_edit(request, pk):
    resource = Resource.objects.get(pk=pk)
 
    if request.method == 'GET':
        context = {
            'resource': resource,
            'form': ResourceForm(instance=resource)
        }
        return render(request, 'edit.html', context)
    else:
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('index')
 
        context = {
            'resource': resource,
            'form': form,
        }
        return render(request, 'edit.html', context)
 
 
def resource_details(request, pk):
    resource = Resource.objects.get(pk=pk)
    ingredients = resource.ingredients.split(', ')
    context = {
        'resource': resource,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
 
 
def resource_delete(request, pk):
    resource = Resource.objects.get(pk=pk)
 
    if request.method == 'GET':
        context = {
            'resource': resource,
            'form': DeleteResourceForm(instance=resource)
        }
 
        return render(request, 'delete.html', context)
    else:
        resource.delete()
        return redirect('index')    




# class ResourceView(View):
#     def get(self, request, comment_id):
#         '''GET the commentupdate view of a single task on the todo list'''
#         task_object = Task.objects.get(id=comment_id)
#         task_form = CommentForm(instance=task_object)

#         comments = UserComment.objects.filter(task=task_object).order_by('-created_at')
#         comment_form = UserCommentForm(task=task_object)

#         tags = task_object.tags.all()  # Tag.objects.filter(task=task)
#         tag_form = TagForm(task=task_object)

#         return render(
#             request=request,
#             template_name='admin.html',
#             context={
#                 'task_form': task_form,
#                 'id': comment_id,
#                 'comments': comments,
#                 'tags': tags,
#                 'comment_form': comment_form,
#                 'tag_form': tag_form,
#             }
#         )

#     def post(self, request, comment_id):
#         '''Update or delete the specific task based on what the user submitted in the form'''
#         task = Task.objects.get(id=comment_id)     

#         # Check request.POST to see which button the user clicked, and run the related logic
#         if 'save_task' in request.POST:
#             task_form = CommentForm(request.POST, instance=task)
#             task_form.save()

#         elif 'delete_task' in request.POST:
#             task.delete()

#         elif 'save_comment' in request.POST:
#             # The user clicked the button to add a comment, not update the task
#             comment_form = CommentForm(request.POST, task=task)
#             comment_form.save()

#             # In this case, we don't want to go back to the homepage, reload the 
#             # current page instead
#             return redirect('task', comment_id=task.id)

#         elif 'add_tag' in request.POST:
#             tag_form = TagForm(request.POST, task=task)
#             tag_form.save()

#             return redirect('task', comment_id=task.id)

#         elif 'complete' in request.POST:
#             task.completed = True
#             task.save()

#         # "redirect" to the todo homepage
#         return redirect('comment_list')

# class ResourceReviewView(View):
#     def rate(request, id):
#         post = Resource.objects.get(id=comment_id)
#         form = ResourceReviewForm(request.POST or None)
#         if form.is_valid():
#             user_name = request.POST.get('user_name')
#             resource_stars = request.POST.get('resource_stars')
#             resourcereview_comment = request.POST.get('resourcereview_comment')
#             review = ResourceReview(user_name = user_name, resource_stars = resource_stars,  resourcereview_comment=resourcereview_comment, resource=post)
#             review.save()
#             return redirect('success')

#         form = ResourceReviewForm()
#         context = {
#             "form":form

#         }
#         return render(request, 'mirrormorror/reviews_comments.html',context)

class CategoryListView(View):


    def get(self, request):
        categorys = Category.objects.all().order_by('-id')
        form = CategoryForm()

        return render(
            request=request, template_name = 'category.html', context = {'categorys': categorys, 'form': form}
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
        '''GET the detail view of a single task on the todo list'''
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



