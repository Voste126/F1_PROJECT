# data_processing/fetch_data.py

import fastf1
import pandas as pd

def get_race_session_data(year, event, session_type):
    """
    Fetches the race session data using FastF1 and converts laps to a DataFrame.
    
    Args:
        year (int): The race season year.
        event (str): The name of the Grand Prix event.
        session_type (str): The session type (e.g., 'Q' for qualifying, 'R' for race).
    
    Returns:
        pd.DataFrame: DataFrame containing lap data, or None if an error occurs.
    """
    try:
        session = fastf1.get_session(year, event, session_type)
        session.load(telemetry=False)  # Disable telemetry if not needed for faster loading
        
        laps = session.laps
        # Filter and convert only those laps that have the to_dict() method
        laps_data = [lap.to_dict() for lap in laps if hasattr(lap, 'to_dict')]
        
        if not laps_data:
            print("No lap data available after filtering.")
            return None
        
        laps_df = pd.DataFrame(laps_data)
        return laps_df
    except Exception as e:
        print(f"Error fetching race data: {e}")
        return None

# FastF1 might take a little while to fetch and process data. 
# In a production app, you may want to handle such delays asynchronously or cache the data.