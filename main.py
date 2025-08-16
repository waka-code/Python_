from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from database import connect_to_mongo, close_mongo_connection
from config import get_settings
from routers import items

# Obtener configuración
settings = get_settings()


@asynccontextmanager #define el ciclo de vida de la app
async def lifespan(app: FastAPI):
    # Startup
    print("Iniciando aplicación...")
    await connect_to_mongo()
    yield
    # Shutdown
    print("Cerrando aplicación...")
    await close_mongo_connection()


# Configuración de la aplicación
app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,  # Configurado desde settings
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(items.router, prefix="/api/v1")


@app.get("/", tags=["Health Check"])
async def root():
    return JSONResponse(
        content={
            "message": "FastAPI + MongoDB Atlas API funcionando correctamente",
            "version": settings.api_version,
            "status": "healthy",
            "database": "MongoDB Atlas"
        }
    )


@app.get("/health", tags=["Health Check"])
async def health_check():
    return JSONResponse(
        content={
            "status": "healthy",
            "database": "MongoDB Atlas - connected",
            "version": settings.api_version,
            "environment": "production" if "mongodb+srv" in settings.mongodb_url else "development"
        }
    )
