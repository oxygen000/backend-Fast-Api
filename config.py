import os

# API configuration
API_HOST = os.environ.get("API_HOST", "0.0.0.0")
API_PORT = int(os.environ.get("API_PORT", 8000))
API_DEBUG = os.environ.get("API_DEBUG", "False").lower() == "true"
API_VERSION = "1.0.0"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "app.log")

# Make sure logs directory exists
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs"), exist_ok=True)

# Database configuration
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "face_recognition.db")

# Make sure the data directory exists
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), exist_ok=True)

# Set this to True to recreate the database and rebuild recognition models
# WARNING: This will delete all existing data
REBUILD_DATABASE = False

# Set a longer timeout for database operations (in milliseconds)
DB_TIMEOUT = 10000  # 10 seconds

# Cache expiry time in seconds
CACHE_EXPIRY = 60 * 5  # 5 minutes

# Create a config object that can be imported elsewhere
class Configuration:
    def __init__(self):
        self.API_HOST = API_HOST
        self.API_PORT = API_PORT
        self.API_DEBUG = API_DEBUG 
        self.API_VERSION = API_VERSION
        self.LOG_LEVEL = LOG_LEVEL
        self.LOG_FORMAT = LOG_FORMAT
        self.LOG_FILE = LOG_FILE
        self.DB_PATH = DB_PATH
        self.REBUILD_DATABASE = REBUILD_DATABASE
        self.DB_TIMEOUT = DB_TIMEOUT
        self.CACHE_EXPIRY = CACHE_EXPIRY

# Create an instance of the config class
config = Configuration() 