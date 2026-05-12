from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.domain.exceptions.exception_scheduling import (
    NotFoundScheduling, 
    FindScheduling,
    AlreadyExistsScheduling,
    NotSucessCreateScheduling,
    NotSucessDeleteScheduling,
    NotSucessUpdateScheduling
)

def scheduling_handle_exception(app):
    
    @app.exception_handler(NotFoundScheduling)
    async def notfound_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(FindScheduling)
    async def find_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(AlreadyExistsScheduling)
    async def already_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessCreateScheduling)
    async def notsucess_create_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessUpdateScheduling)
    async def notsucess_update_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessDeleteScheduling)
    async def notsucess_delete_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )    
    
    return {
        notfound_handle_exception,
        find_handle_exception,
        already_handle_exception,
        notsucess_create_handle_exception,
        notsucess_update_handle_exception,
        notsucess_delete_handle_exception
    }