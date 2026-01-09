import json
import os
from datetime import datetime

# This is a simplified mock-up of the logic to save data
# Ensure your AISStream logic feeds into the 'new_data' variable
def save_vessel_data(lat, lon, name="My Vessel"):
    file_name = 'vessels.json'
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    
    new_entry = {
        "timestamp": timestamp,
        "name": name,
        "lat": lat,
        "lon": lon
    }

    # Load existing data or start a new list
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
    else:
        data = []

    # Keep only the last 100 positions to save space
    data.append(new_entry)
    data = data[-100:]

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage (Replace with your actual AIS parsing logic)
save_vessel_data(51.505, -0.09) 
#1
