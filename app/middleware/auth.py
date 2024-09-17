from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.auth import AuthService

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token:
            auth_service = AuthService()
            token_data = auth_service.decode_access_token(token)
            if not token_data:
                raise HTTPException(status_code=401, detail="Invalid token")
            request.state.user = token_data
        else:
            request.state.user = None
        response = await call_next(request)
        return response
