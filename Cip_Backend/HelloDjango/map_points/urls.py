from django.urls import path
from . import views


urlpatterns = [
    path('points/<region>/<point_type>/', views.MapPointsListView.as_view()),
    path('regions/', views.RegionsListView.as_view()),
    path('types/', views.PointTypesListView.as_view())
]