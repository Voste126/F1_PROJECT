# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('race-data/', views.race_data, name='race-data'),
    path('search/', views.search_race_data, name='search-race-data'),
    path('lap/<int:lap_number>/', views.lap_detail, name='lap-detail'),
]

