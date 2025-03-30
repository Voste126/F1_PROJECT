# dashboard/views.py

from django.shortcuts import render
from data_processing.fetch_data import get_race_session_data

def home(request):
    context = {
        'message': 'Welcome to the F1 Dashboard!'
    }
    return render(request, 'dashboard/home.html', context)

def race_data(request):
    # Parameters for fetching session data (adjust these as needed)
    year = 2021
    event = 'Italian Grand Prix'
    session_type = 'R'  # 'R' indicates the race session
    
    # Get the laps data as a Pandas DataFrame
    laps_df = get_race_session_data(year, event, session_type)
    
    if laps_df is not None:
        # Convert the DataFrame to HTML for display
        race_data_html = laps_df.to_html(classes="table table-striped", border=0)
    else:
        race_data_html = "<p>Race data is not available at this time.</p>"
    
    context = {'race_data': race_data_html}
    return render(request, 'dashboard/race_data.html', context)
