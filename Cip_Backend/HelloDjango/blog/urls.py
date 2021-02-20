from django.urls import path
from . import views

urlpatterns = [
    path('get_future_posts/', views.FuturePostsListView.as_view()),
    path('detail/<slug:slug>/', views.PostDetailView.as_view()),
    path('create_comment/', views.CreateCommentView.as_view()),
    path('', views.PostsListView.as_view())
]