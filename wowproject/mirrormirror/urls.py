from django.urls import path

from mirrormirror.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path("ace-quiz/", AceQuizView.as_view(), name='ace-quiz'),
    path("score_stats/", ScoreStatsView.as_view(), name='score_stats'),

    path('comment/', UserCommentListView.as_view(), name='comment_list'),
    path('<int:comment_id>', UserCommentDetailView.as_view(), name='updateordelete'),

]
# handler404 = 'mirrormirror.views.handler404'
