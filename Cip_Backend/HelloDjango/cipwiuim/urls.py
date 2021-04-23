from django.urls import path
from . import views


urlpatterns = [
    path('partner_forms/<slug:slug>/', views.PartnerFormDetail.as_view(),),
    path('about/', views.AboutCipView.as_view()),
    path('rules/', views.RulesView.as_view()),
    path('questions/', views.QuestionsView.as_view()),
    path('gallery/', views.GalleryView.as_view()),
    path('', views.MainLayoutData.as_view()),
]