from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainLayoutData.as_view()),
]