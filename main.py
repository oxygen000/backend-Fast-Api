"""
Main entry point for the Face Recognition API.
"""

import uvicorn
import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).resolve().parent))

# ✅ استيراد المتغيرات من config.py
import config
from utils.logger import get_logger

# Get logger
logger = get_logger("main")

def main():
    """
    Main entry point for the application.
    """
    # Fly.io provides PORT environment variable
    port = int(os.environ.get("PORT", 8000))  # حدد 8000 افتراضياً

    logger.info("Starting Face Recognition API")
    logger.info(f"Host: 0.0.0.0, Port: {port}")
    
    # Start the server
    uvicorn.run(
        "api.api:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
