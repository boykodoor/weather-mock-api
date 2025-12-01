import json
from utils.formatter import format_response

with open("mock-data/weather_today.json", "r") as f:
    data = json.load(f)

print(format_response(data))
