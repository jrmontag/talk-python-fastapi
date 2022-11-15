from typing import Optional

from fastapi import APIRouter, Depends
from models.location import Location
from pydantic import BaseModel

from services import openweather_service

router = APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str]='metric'):    
    report = openweather_service.get_report(loc.city, loc.state, loc.country, units)
    
    return report 
