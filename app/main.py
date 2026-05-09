from fastapi import FastAPI

from app.infrastructure.database.connection import Base, engine
from app.interface.handler.exception_service import Service_exception_handler
from app.interface.api.service_controller import router as service_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

Service_exception_handler(app)
app.include_router(service_router)
