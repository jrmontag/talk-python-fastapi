from typing import Optional

import requests

api_key: Optional[str] = None 

def get_report(city: str, state: Optional[str], country: str, units: Optional[str] = 'metric'):
    # API v2.5 endpoints are deprecated: https://openweathermap.org/current#name    
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    print(url)
    
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    forecast = data['main']
    
    return forecast
