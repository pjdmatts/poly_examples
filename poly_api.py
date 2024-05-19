# Experimenting with the API directly

import requests
import constants
import json

params = {'ticker': 'GE', 'timeframe': 'annual', 'limit': 100, 'apiKey': constants.key}
response = requests.get('https://api.polygon.io/vX/reference/financials', params=params)
data = response.json()

json_object = json.dumps(data)

with open("financials.json", "w") as outfile:
    outfile.write(json_object)