# dashboard/views.py

from django.shortcuts import render
from .forms import RaceDataForm
from data_processing.fetch_data import get_race_session_data
import fastf1

def home(request):
    context = {
        'message': 'Welcome to the F1 Dashboard!'
    }
    return render(request, 'dashboard/home.html', context)

def race_data(request):
    """
    This view remains as a demo view with hard-coded parameters.
    """
    year = 2021
    event = 'Italian Grand Prix'
    session_type = 'R'
    
    laps_df = get_race_session_data(year, event, session_type)
    race_data_html = (
        laps_df.to_html(classes="table table-striped", border=0)
        if laps_df is not None else "<p>Race data is not available at this time.</p>"
    )
    
    return render(request, 'dashboard/race_data.html', {'race_data': race_data_html})

def search_race_data(request):
    """
    View to handle user input for race data search.
    """
    if request.method == "POST":
        form = RaceDataForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            event = form.cleaned_data['event']
            session_type = form.cleaned_data['session_type']
            
            laps_df = get_race_session_data(year, event, session_type)
            race_data_html = (
                laps_df.to_html(classes="table table-striped", border=0)
                if laps_df is not None else "<p>No data available for the given parameters.</p>"
            )
            return render(request, 'dashboard/race_data.html', {'race_data': race_data_html})
    else:
        form = RaceDataForm()
    
    return render(request, 'dashboard/search_race_data.html', {'form': form})

# dashboard/views.py
from django.http import HttpResponse
from django.shortcuts import render
import fastf1
from data_processing.fetch_data import get_race_session_data

def lap_detail(request, lap_number):
    """
    Detailed view for a specific lap's telemetry data.
    """
    # Parameters: In a real scenario, you might pass these via GET parameters or session data.
    year = 2021
    event = 'Italian Grand Prix'
    session_type = 'R'
    
    # Load the session with telemetry enabled
    session = fastf1.get_session(year, event, session_type)
    session.load()  # Load all data including telemetry

    # Find the lap object matching the provided lap_number
    lap_obj = None
    for lap in session.laps:
        if hasattr(lap, 'to_dict'):
            lap_info = lap.to_dict()
            if lap_info.get('LapNumber') == lap_number:
                lap_obj = lap
                break
    
    if lap_obj is None:
        return HttpResponse("Lap object not found.", status=404)
    
    # Extract telemetry data from the lap.
    # Adjust the frequency and the columns according to your needs.
    telemetry = lap_obj.get_telemetry(frequency='original')
    
    # Convert telemetry data to lists for charting
    # (Assuming telemetry is a DataFrame with columns 'Time' and 'Speed'. Adjust as necessary.)
    time_data = telemetry['Time'].dt.total_seconds().tolist() if 'Time' in telemetry.columns else []
    speed_data = telemetry['Speed'].tolist() if 'Speed' in telemetry.columns else []
    
    context = {
        'lap_number': lap_number,
        'time_data': time_data,
        'speed_data': speed_data,
    }
    return render(request, 'dashboard/lap_detail.html', context)
