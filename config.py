import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings:
    
    def __init__(self):
        # Base de datos
        self.mongodb_url = os.getenv( "MONGODB_URL" )
        self.database_name = os.getenv("DATABASE_NAME", "fastapi_db")
        
        # API
        self.api_title = os.getenv("API_TITLE", "FastAPI CRUD con MongoDB")
        self.api_description = os.getenv("API_DESCRIPTION", "API RESTful para gestión de items")
        self.api_version = os.getenv("API_VERSION", "1.0.0")
        
        # CORS
        allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "*")
        self.allowed_origins = [origin.strip() for origin in allowed_origins_str.split(",")]
        
        # Paginación
        self.default_page_size = int(os.getenv("DEFAULT_PAGE_SIZE", "10"))
        self.max_page_size = int(os.getenv("MAX_PAGE_SIZE", "100"))
        
        # Logging
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

# Caching es una especie de useMemo
@lru_cache()
def get_settings() -> Settings:
    return Settings()
