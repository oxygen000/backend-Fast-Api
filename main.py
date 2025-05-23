"""
Main entry point for the Face Recognition API.
"""

import uvicorn
import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).resolve().parent))

# Import config and logger
from config import config
from src.utils.logger import get_logger

# Get logger
logger = get_logger("main")

def main():
    """
    Main entry point for the application.
    """
    # Fly.io provides PORT environment variable
    port = int(os.environ.get("PORT", config.API_PORT))

    logger.info(f"Starting Face Recognition API v{config.API_VERSION}")
    logger.info(f"Host: {config.API_HOST}, Port: {port}")
    
    # Start the server
    uvicorn.run(
        "src.api.api:app",
        host=config.API_HOST,
        port=port,
        reload=config.API_DEBUG,
        log_level=config.LOG_LEVEL.lower()
    )

if __name__ == "__main__":
    main()
