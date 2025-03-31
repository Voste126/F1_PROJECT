# dashboard/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Race, LapTime, FantasyTeam, Driver, FantasyScore
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, 'dashboard/home.html', {'message': 'Welcome to the F1 Dashboard!'})

def historical_comparison_view(request):
    # Fetch all races
    races = Race.objects.all()

    # If a comparison is requested
    race_ids = request.GET.getlist('race_ids')
    comparison_data = []
    if race_ids:
        for race_id in race_ids:
            race = Race.objects.get(id=race_id)
            lap_times = LapTime.objects.filter(race=race)
            lap_df = pd.DataFrame(list(lap_times.values('driver__name', 'lap_number', 'lap_time')))
            comparison_data.append({'race': race, 'lap_data': lap_df})

    return render(request, 'dashboard/historical_comparison.html', {
        'races': races,
        'comparison_data': comparison_data
    })

@login_required
def create_fantasy_team_view(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        driver_ids = request.POST.getlist('drivers')
        
        # Create the fantasy team
        fantasy_team = FantasyTeam.objects.create(user=request.user, name=team_name)
        fantasy_team.drivers.set(Driver.objects.filter(id__in=driver_ids))
        
        return redirect('fantasy_team_detail', team_id=fantasy_team.id)

    drivers = Driver.objects.all()
    return render(request, 'dashboard/create_fantasy_team.html', {'drivers': drivers})

def leaderboard_view(request):
    # Fetch all fantasy scores and order by total score
    leaderboard = FantasyScore.objects.values('fantasy_team__name').annotate(total_score=models.Sum('score')).order_by('-total_score')

    return render(request, 'dashboard/leaderboard.html', {'leaderboard': leaderboard})

def driver_profile_view(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'dashboard/driver_profile.html', {'driver': driver})


def team_profile_view(request, team_id):
    return HttpResponse(f"Team Profile for Team ID: {team_id}")
