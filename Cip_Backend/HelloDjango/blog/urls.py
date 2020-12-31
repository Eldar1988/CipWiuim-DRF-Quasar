from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view())
]