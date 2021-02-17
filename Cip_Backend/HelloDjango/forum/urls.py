from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:slug>/', views.ThemeDetailView.as_view()),
    path('create_answer/', views.CreateAnswerView.as_view()),
    path('', views.ThemesListView.as_view()),
]