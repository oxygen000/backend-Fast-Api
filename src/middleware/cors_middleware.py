"""
CORS middleware for the Face Recognition API.
Handles Cross-Origin Resource Sharing (CORS) for the API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from pathlib import Path

# Import config and logger
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from config import config
from src.utils.logger import get_logger

# Get logger
logger = get_logger("cors_middleware")

def setup_cors(app: FastAPI) -> None:
    """
    Set up CORS middleware for the application.
    
    Args:
        app: The FastAPI application
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=config.CORS_CREDENTIALS,
        allow_methods=config.CORS_METHODS,
        allow_headers=config.CORS_HEADERS,
    )
    
    logger.info(f"CORS middleware initialized with origins: {config.CORS_ORIGINS}")
