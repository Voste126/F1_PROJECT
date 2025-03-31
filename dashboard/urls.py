# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
]

urlpatterns += [
    path('driver/<int:driver_id>/', views.driver_profile_view, name='driver_profile'),
    path('team/<int:team_id>/', views.team_profile_view, name='team_profile'),
    path('team/<int:team_id>/', views.driver_profile_view, name='team_profile'),
]

urlpatterns += [
    path('historical-comparison/', views.historical_comparison_view, name='historical_comparison'),
]

urlpatterns += [
    path('fantasy-team/create/', views.create_fantasy_team_view, name='create_fantasy_team'),
]

urlpatterns += [
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]

