from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from config import get_settings

# Obtener configuración
settings = get_settings()

class Database:
    client: AsyncIOMotorClient = None
    
database = Database()

async def get_database():
    return database.client[settings.database_name]

async def connect_to_mongo():
    database.client = AsyncIOMotorClient(
        settings.mongodb_url, 
        server_api=ServerApi('1'),
        uuidRepresentation="standard",
        maxPoolSize=10,
        minPoolSize=1,
        maxIdleTimeMS=30000,
        connectTimeoutMS=10000,
        serverSelectionTimeoutMS=5000
    )
    # Verificar conexión
    try:
        await database.client.admin.command('ping')
        print(f"Conectado exitosamente a MongoDB Atlas: {settings.database_name}")
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        raise

async def close_mongo_connection():
    if database.client:
        database.client.close()
        print("🔌 Desconectado de MongoDB Atlas")
