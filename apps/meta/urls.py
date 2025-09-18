from django.urls import path
from apps.meta.api_endpoints import watchsession,comment
from apps.meta.api_endpoints.comment.CommentList.views import CommentListView

urlpatterns = [
    path('watch-session-create/',
         watchsession.WatchSessionCreateView.as_view(),
         name='watch_session_create'),
    path('comment-create/',comment.CommentCreateView.as_view(),name='comment-create'),
    path('comment-list/',CommentListView,name='comment')
]