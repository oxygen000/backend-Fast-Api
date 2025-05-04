import os

# API configuration
API_HOST = os.environ.get("API_HOST", "0.0.0.0")
API_PORT = int(os.environ.get("API_PORT", 8000))
API_DEBUG = os.environ.get("API_DEBUG", "False").lower() == "true"
API_VERSION = "1.0.0"
API_TITLE = "Face Recognition API"
API_DESCRIPTION = "API for face recognition and registration"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "app.log")

# CORS configuration
CORS_ORIGINS = ["*"]  # Allow all origins
CORS_METHODS = ["*"]  # Allow all methods
CORS_HEADERS = ["*"]  # Allow all headers
CORS_CREDENTIALS = True  # Allow credentials

# Make sure logs directory exists
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs"), exist_ok=True)

# Database configuration
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "face_recognition.db")

# Make sure the data directory exists
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), exist_ok=True)

# Upload directory
UPLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Set this to True to recreate the database and rebuild recognition models
# WARNING: This will delete all existing data
REBUILD_DATABASE = False

# Set a longer timeout for database operations (in milliseconds)
DB_TIMEOUT = 10000  # 10 seconds

# Cache expiry time in seconds
CACHE_EXPIRY = 60 * 5  # 5 minutes
CACHE_TTL = CACHE_EXPIRY  # Alias for CACHE_EXPIRY to maintain compatibility
CACHE_ENABLED = True  # Enable caching

# Face recognition settings
FACE_RECOGNITION_TOLERANCE = 0.6  # Lower is more strict
FACE_RECOGNITION_MODEL = os.environ.get("FACE_RECOGNITION_MODEL", "hog")  # "hog" or "cnn"
FACE_ENCODING_JITTERS = 5
MULTI_ANGLE_JITTER = 15
MAX_CONCURRENT_RECOGNITIONS = 5

# Create a config object that can be imported elsewhere
class Configuration:
    def __init__(self):
        self.API_HOST = API_HOST
        self.API_PORT = API_PORT
        self.API_DEBUG = API_DEBUG 
        self.API_VERSION = API_VERSION
        self.API_TITLE = API_TITLE
        self.API_DESCRIPTION = API_DESCRIPTION
        self.LOG_LEVEL = LOG_LEVEL
        self.LOG_FORMAT = LOG_FORMAT
        self.LOG_FILE = LOG_FILE
        self.CORS_ORIGINS = CORS_ORIGINS
        self.CORS_METHODS = CORS_METHODS
        self.CORS_HEADERS = CORS_HEADERS
        self.CORS_CREDENTIALS = CORS_CREDENTIALS
        self.DB_PATH = DB_PATH
        self.UPLOADS_DIR = UPLOADS_DIR
        self.REBUILD_DATABASE = REBUILD_DATABASE
        self.DB_TIMEOUT = DB_TIMEOUT
        self.CACHE_EXPIRY = CACHE_EXPIRY
        self.CACHE_TTL = CACHE_TTL
        self.CACHE_ENABLED = CACHE_ENABLED
        self.FACE_RECOGNITION_TOLERANCE = FACE_RECOGNITION_TOLERANCE
        self.FACE_RECOGNITION_MODEL = FACE_RECOGNITION_MODEL
        self.FACE_ENCODING_JITTERS = FACE_ENCODING_JITTERS
        self.MULTI_ANGLE_JITTER = MULTI_ANGLE_JITTER
        self.MAX_CONCURRENT_RECOGNITIONS = MAX_CONCURRENT_RECOGNITIONS

# Create an instance of the config class
config = Configuration() 