import os

class Config:
    """Configuración base para la aplicación Flask."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))

class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
