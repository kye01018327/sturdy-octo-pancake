import googlemaps
import datetime
import csv
import time
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Setup your API Key
API_KEY = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=API_KEY)

# 2. Define your origin and destination
origin = os.getenv("HOME_ADDR")
destination = os.getenv("WORK_ADDR")

print(API_KEY, origin, destination, sep="\n")

# 3. Prepare data collection
results = []
# Start from the next top or half-hour mark
now = datetime.datetime.now()
start_time = now.replace(second=0, microsecond=0)
if start_time.minute < 30:
    start_time = start_time.replace(minute=30)
else:
    start_time = (start_time + datetime.timedelta(hours=1)).replace(minute=0)

print(f"Fetching traffic data for 24 hours starting from {start_time}...")

# 48 intervals of 30 minutes = 24 hours
for i in range(48):
    departure_time = start_time + datetime.timedelta(minutes=30 * i)
    
    # Request distance matrix with departure_time
    response = gmaps.distance_matrix(
        origins=origin,
        destinations=destination,
        mode="driving",
        departure_time=departure_time,
        traffic_model="best_guess"
    )
    
    # Parse duration in traffic
    element = response['rows'][0]['elements'][0]
    if element['status'] == 'OK':
        duration = element['duration_in_traffic']['value'] / 60  # convert to minutes
        results.append([departure_time.strftime('%Y-%m-%d %H:%M'), duration])
        print(f"Time: {departure_time.strftime('%H:%M')} | Est. Commute: {round(duration, 1)} mins")
    
    # Pause slightly to be respectful of API rate limits
    time.sleep(0.25)

# 4. Save to CSV
with open('./datasets/commute_work_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Duration_Minutes"])
    writer.writerows(results)

print("Done! Data saved to commute_work_data.csv")