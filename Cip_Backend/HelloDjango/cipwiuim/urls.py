from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainLayoutData.as_view()),
    path('get_testimonials/', views.TestimonialsListView.as_view())     # Отзывы о компании Cip
]