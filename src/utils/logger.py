"""
Logger module for the Face Recognition API.
Provides a consistent logging interface for the application.
"""

import logging
import sys
import os
from pathlib import Path
from typing import Optional

# Import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from config import config

# Create logs directory if it doesn't exist
logs_dir = os.path.join(Path(__file__).resolve().parent.parent.parent, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Set log file path
LOG_FILE = os.path.join(logs_dir, "app.log")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Create logger
logger = logging.getLogger("face_recognition_api")
logger.setLevel(getattr(logging, config.LOG_LEVEL))

# Create formatter
formatter = logging.Formatter(LOG_FORMAT)

# Create file handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance with the given name.
    If no name is provided, returns the root logger.
    
    Args:
        name: The name of the logger
        
    Returns:
        A logger instance
    """
    if name:
        return logging.getLogger(f"face_recognition_api.{name}")
    return logger
