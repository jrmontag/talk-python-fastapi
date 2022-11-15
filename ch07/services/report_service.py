import datetime
from typing import List
from uuid import uuid4
import uuid
from models.reports import Report
from models.location import Location

# use an in-memory storage for this demo app
__reports: List[Report] = []

async def get_reports() -> List[Report]:
    # db read would be async 
    return list(__reports)


async def add_report(description: str, location: Location):
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()), 
        location=location, 
        description=description, 
        created_date=now)

    # db write would be async
    __reports.append(report)
    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report
