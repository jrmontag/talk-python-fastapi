import fastapi

router = fastapi.APIRouter()

@router.get('/api/weather/')
def weather():
    return "some weather report"
