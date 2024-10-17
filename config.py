import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Default to SQLite for local testing
    SQLALCHEMY_DATABASE_URI = os.getenv('AZURE_SQL_CONNECTION_STRING', 'sqlite:///database.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AZURE_BLOB_CONNECTION_STRING = os.getenv('AZURE_BLOB_CONNECTION_STRING')
    AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
    AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
    AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
