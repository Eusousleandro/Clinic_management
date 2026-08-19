from fastapi import FastAPI

from app.infrastructure.database.connection import Base, engine
from app.interface.handler.exception_service import Service_exception_handler
from app.interface.api.service_controller import router as service_router
from app.interface.api.scheduling_controller import router as scheduling_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

Service_exception_handler(app)
app.include_router(service_router)
app.include_router(scheduling_router)