"""
Configuration file for Bus Fare Aggregator application
"""

import os

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    FLASK_ENV = 'production'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Supported cities for bus routes
SUPPORTED_CITIES = {
    'origin': ['Bengaluru', 'Chennai', 'Coimbatore', 'Hyderabad', 'Mumbai'],
    'destination': ['Coimbatore', 'Chennai', 'Bengaluru', 'Madurai', 'Kochi']
}

# Booking platforms
PLATFORMS = ['RedBus', 'AbhiBus', 'MakeMyTrip']

# API timeout (seconds)
API_TIMEOUT = 10

# Maximum retries for failed API calls
MAX_RETRIES = 3