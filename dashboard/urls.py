# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('race-data/', views.race_data, name='race-data'),
]

