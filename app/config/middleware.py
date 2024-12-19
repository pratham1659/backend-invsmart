from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import time
import logging

# Configure the logger explicitly
logger = logging.getLogger("uvicorn.access")
logger.setLevel(logging.INFO)

# Ensure no handlers are added multiple times
if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        processing_time = time.time() - start_time

        # Construct the log message
        message = (
            f"{request.client.host} - {request.method} - {request.url.path} - "
            f"{response.status_code} completed after {processing_time:.2f}s"
        )

        print(message)

        return response

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Be cautious with "*" in production
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    # Add TrustedHostMiddleware to guard against HTTP Host Header attacks
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"]  # Be strict in production, avoid using "*"
    )
