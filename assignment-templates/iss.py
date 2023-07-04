import requests
import matplotlib
from time import sleep 

longitude = []
latitude = []
timestamp = []

for i in range(100):
    r = requests.get('http://api.open-notify.org/iss-now.json')
    longitude.append(r.json()["iss_position"]["longitude"])
    latitude.append(r.json()["iss_position"]["latitude"])
    timestamp.append(r.json()["timestamp"])
    print(f"Done: {i + 1}/100")
    sleep(10)

print(longitude)
print(latitude) 
print(timestamp)