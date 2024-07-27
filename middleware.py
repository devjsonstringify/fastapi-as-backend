"""
This module contains middleware for logging HTTP requests and responses.

It defines the LoggingMiddleware class, which logs the method and URL of
incoming requests and the status code of outgoing responses.
"""

import logging
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    """_summary"""
    async def dispatch(self, request, call_next):
        logger = logging.getLogger("uvicorn")
        # Use lazy formatting with % operator
        logger.info("Request: %s %s", request.method, request.url)
        response = await call_next(request)
        logger.info("Response: %s", response.status_code)
        return response
