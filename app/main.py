from fastapi import FastAPI

from app.interface.api.service_controller import router as service_router

app = FastAPI()

app.include_router(service_router)