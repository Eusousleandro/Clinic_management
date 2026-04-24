from app.infrastructure.database.models.service_model import Service
from app.interface.schemas.service_schema import ServiceResponse

def to_service_response(service: Service) -> ServiceResponse:
    return ServiceResponse(
        id=service.id,
        name=service.name,
        duration_minutes=service.duration_minutes,
        price=service.price
    )