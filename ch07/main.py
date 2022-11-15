import asyncio
import json
from pathlib import Path
import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services.report_service import add_report
from models.location import Location
from services import openweather_service, report_service
from views import home

api = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_api_keys()
    configure_fake_data()

def configure_routing():    
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)

def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"Warning: {file} not found. See settings_template.json")
        raise Exception("settings.json file not found, API keys are required.")

    with file.open() as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get('api_key')

def configure_fake_data():
    # helps with testing /api/reports
    loc = Location(city='Denver', state="CO", country="US")
    asyncio.run(report_service.add_report('2" of snow this morning', loc))
    asyncio.run(report_service.add_report('Sunshine is quickly melting things!', loc))


if __name__ == '__main__':
    # devel
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    # prod
    configure()
