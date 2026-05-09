from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.domain.exceptions.exception import (
    findHandleException,
    notFoundHandleException,
    alreadyExistsHandleException,
    createHandleException,
    updateHandleException,
    deleteHandleException
)

def Service_exception_handler(app):

    @app.exception_handler(notFoundHandleException)
    async def notfound_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(findHandleException)
    async def find_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app
    async def already_exists_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )

    @app.exception_handler(createHandleException)
    async def create_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(updateHandleException)
    async def update_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )

    @app.exception_handler(deleteHandleException)
    async def delete_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )
    
