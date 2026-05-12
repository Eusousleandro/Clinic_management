from app.infrastructure.database.models.scheduling_model import Scheduling
from app.interface.schemas.scheduling_schemas import SchedulingResponse

def to_scheduling_response(scheduling: Scheduling) -> SchedulingResponse:
    return SchedulingResponse(
        id=scheduling.id,
        name=scheduling.name,
        description=scheduling.description,
        start_time=scheduling.start_time,
        end_time=scheduling.end_time
    )