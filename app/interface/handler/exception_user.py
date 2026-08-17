from fastapi import  Request, status
from fastapi.responses import JSONResponse

from app.domain.exceptions.exception_user import (
    NotFoundUser,
    FindUser,
    AlreadyExistsUser,
    NotSucessCreateUser,
    NotSucessDeleteUser,
    NotSucessUpdateUser,
    NotAuthenticationUser
)

def scheduling_handle_exception(app):
    
    @app.exception_handler(NotFoundUser)
    async def notfound_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(FindUser)
    async def find_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(AlreadyExistsUser)
    async def already_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessCreateUser)
    async def notsucess_create_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessUpdateUser)
    async def notsucess_update_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotSucessDeleteUser)
    async def notsucess_delete_handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )
    
    @app.exception_handler(NotAuthenticationUser)
    async def notauthentication_handle_exception(request: Request, exc: Exception):
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
        notsucess_delete_handle_exception,
        notauthentication_handle_exception
    }