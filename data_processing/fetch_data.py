# data_processing/fetch_data.py

import fastf1
import pandas as pd

def get_race_session_data(year, event, session_type):
    """
    Fetches the race session data using FastF1.
    
    Args:
        year (int): The race season year.
        event (str): The name of the Grand Prix event.
        session_type (str): The session type (e.g., 'Q' for qualifying, 'R' for race).
    
    Returns:
        pd.DataFrame: DataFrame containing lap data, or None if an error occurs.
    """
    try:
        # Fetch the session (this downloads and caches data)
        session = fastf1.get_session(year, event, session_type)
        session.load()  # Load all available data
        # Retrieve laps data as a DataFrame
        laps = session.laps
        laps_df = laps.df  # FastF1 provides a Pandas DataFrame
        return laps_df
    except Exception as e:
        print(f"Error fetching race data: {e}")
        return None

# FastF1 might take a little while to fetch and process data. 
# In a production app, you may want to handle such delays asynchronously or cache the data.