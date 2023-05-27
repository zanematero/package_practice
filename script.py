import pprint
import requests
import json
from matplotlib import pyplot as plt
from datetime import datetime

API_URL = 'https://rickandmortyapi.com/api/episode'
city = 'las vegas' # feel free to enter your own city here!
r = requests.get(API_URL)
response = r.json()

episodes = {}

for res in response['results']:
    episodes[res["name"]] = len(res["characters"])
    
print(json.dumps(episodes, indent=4))

plt.xlabel("episode name")
plt.xticks(rotation=40)
plt.ylabel("character count")
plt.plot(episodes.keys(), episodes.values())
plt.show()