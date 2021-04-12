from django.urls import path
from . import views


urlpatterns = [
    path('create_callback/', views.CallBackCreateView.as_view())
]