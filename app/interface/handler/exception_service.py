from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.domain.exceptions.exception import (
    FindHandleException,
    NotFoundHandleException,
    AlreadyExistsHandleException,
    CreateHandleException,
    UpdateHandleException,
    DeleteHandleException
)

def Service_exception_handler(app):

    @app.exception_handler(NotFoundHandleException)
    async def notfound_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(FindHandleException)
    async def find_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(AlreadyExistsHandleException)
    async def already_exists_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )

    @app.exception_handler(CreateHandleException)
    async def create_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(UpdateHandleException)
    async def update_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )

    @app.exception_handler(DeleteHandleException)
    async def delete_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )
    
    return {
        notfound_handle_exception,
        find_handle_exception,
        already_exists_handle_exception,
        create_handle_exception,
        update_handle_exception,
        delete_handle_exception
    }