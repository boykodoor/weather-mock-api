def format_response(data: dict):
    return f"{data['location']}: {data['temperature_c']}°C, {data['condition']}, wind {data['wind_kph']} kph"
