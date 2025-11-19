# ---------------------------------------------------------
# Configuration File
# ----------------------------------------------------------
# Loads environment variables from .env file
# and makes them available as constants for database connections.

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

#MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI")

#MySQL connection details
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
