from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mirrormirror.views import *

urlpatterns = [
    # Home page: has "Mirror Mirror" title, "Click to Begin" button to take to Welcome page, trigger warning, and first healing carousel
    path('', HomeView.as_view(), name='home'),

    # Welcome page: describes "ACEs"--> adverse childhood experiences, "Take Quiz" button to take to Ace-Quiz page, and second healing carousel
    path('welcome/', WelcomeView.as_view(), name='welcome'),

    # Ace-Quiz page: quiz instructions, quiz questions with yes/no radio buttons, "What's My Score" button to calculate results, "ACE Statistics" button
    # to take to stats page, and third healing carousel 
    path("ace-quiz/", AceQuizView.as_view(), name='ace-quiz'),

    # Stats page: lists statistics related to ACE scores both general and based on gender + orientation/s, "Resources" button to take to Resources page
    path("score_stats/", ScoreStatsView.as_view(), name='score_stats'),

    # Resources page: nav menu with resource categories, reassurance text for user, fourth healing carousel, and "Leave Review/Comment" button to take
    # user to reviews and comments page
    path('resources/', ResourcesView.as_view(), name='resources'),
    # Each path for resource categories will display resources specific to that category- zipcode path is different
    path('mentalhealth/', MentalHealthView.as_view(), name='mental health'),
    path('justiceimpacted/', JusticeImpactedView.as_view(), name='justice impacted'),
    path('physicalhealth/', PhysicalHealthView.as_view(), name='physical health'),
    path('overallwellness/', OverallWellnessView.as_view(), name='overall wellness'),
    path('nationalresources/', NationalResourcesView.as_view(), name='national resources'),
    # Zipcode path will display search box for user to enter a zipcode. If resource is present with zipcode identical to user input, resource appears. If there's
    # no resource with zipcode matching user input, nothing appears. If user hits enter without entering digits into search, all resources are displayed
    path('zipcode/', ZipcodeView.as_view(), name='zipcode'),
    path("zipcode/results/", ZipResultsView.as_view(), name="zip search results"),


    # The following paths are for developer use only; not for user interaction. -->
    # Resource Temp Page: displays resources as they've beed added by developers. Allows for resource editing and deletions, as well as option to add more resources
    path('resourcetemppage/', index, name='resourcetemppage'),
    # "Add Resource" button on resource temp page takes to this path. Has form to fill in with resource info and "Create" button adds resource to database
    path('resourcecreate/', resource_create, name='resource create'),
    # "Edit" button on resource temp page takes to this path. Allows developer to edit resource information form or delete resource and updates database based on developer
    # selection
    path('resourceedit/<int:pk>', resource_edit, name='resource edit'),
    # "Delete" button on resource temp page deletes resource from database
    path('delete/<int:pk>', resource_delete, name='resource delete'),

    # "Category Name" text box to type in category name. "Create" button adds category to database and category list
    path('categorycreate/', CategoryListView.as_view(), name='category_list'),
    # Can edit or delete category after clicking on category name. Database is updated based on developer selection
    path('category/<int:category_id>', CategoryDetailView.as_view(), name='updateordeletecategory'),
    # <-- The following paths are for developer use only; not for user interaction.


    # Takes user to reviews_comments page where they have the option to add a resource review, website review, and/or general comment. 
    path('review_comment/', get_and_post, name='display'),
    # The following paths allow user to edit/update or delete their feedback. This will also update the respective databases
    path('resourceereview/<int:review_id>', ResourceReviewDetailView.as_view(), name='edit resource review'),
    path('websitereview/<int:review_id>', WebsiteReviewDetailView.as_view(), name='editsitereview'),
    path('comment/<int:comment_id>', UserCommentDetailView.as_view(), name='updateordelete'),

]
# handler404 = 'mirrormirror.views.handler404'
