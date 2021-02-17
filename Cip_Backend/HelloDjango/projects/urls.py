from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:slug>/', views.ProjectDetailView.as_view()),
    path('', views.ProjectListView.as_view())
]