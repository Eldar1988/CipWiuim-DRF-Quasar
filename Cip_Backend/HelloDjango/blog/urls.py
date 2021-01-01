from django.urls import path
from . import views

urlpatterns = [
    path('get_future_posts/', views.FuturePostsListView.as_view())
]