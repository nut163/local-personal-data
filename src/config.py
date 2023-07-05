import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    API_KEY = os.getenv('API_KEY')