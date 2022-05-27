from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mirrormirror.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path("ace-quiz/", AceQuizView.as_view(), name='ace-quiz'),
    path("score_stats/", ScoreStatsView.as_view(), name='score_stats'),

    path('resources/', ResourcesView.as_view(), name='resources'),
    path('mentalhealth/', MentalHealthView.as_view(), name='mental health'),
    path('justiceimpacted/', JusticeImpactedView.as_view(), name='justice impacted'),
    path('physicalhealth/', PhysicalHealthView.as_view(), name='physical health'),
    path('overallwellness/', OverallWellnessView.as_view(), name='overall wellness'),
    path('nationalresources/', NationalResourcesView.as_view(), name='national resources'),
    path('zipcode/', ZipcodeView.as_view(), name='zipcode'),
    path("zipcode/results/", ZipResultsView.as_view(), name="zip search results"),

    path('resourcetemppage/', index, name='resourcetemppage'),
    path('resourcecreate/', resource_create, name='resource create'),
    path('resourceedit/<int:pk>', resource_edit, name='resource edit'),
    path('delete/<int:pk>', resource_delete, name='resource delete'),

    path('categorycreate/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>', CategoryDetailView.as_view(), name='updateordeletecategory'),

    path('review_comment/', get_and_post, name='display'),
    path('comment/<int:comment_id>', UserCommentDetailView.as_view(), name='updateordelete'),
    path('websitereview/<int:review_id>', WebsiteReviewDetailView.as_view(), name='editsitereview'),
    path('resourceereview/<int:review_id>', ResourceReviewDetailView.as_view(), name='edit resource review'),


    path('resourcereview/', ResourceReviewListView.as_view(), name='resourcereview_list'),
    # path('resourcereview/<int:id>',rate,name='resourcereview_'),
    
]
# handler404 = 'mirrormirror.views.handler404'
