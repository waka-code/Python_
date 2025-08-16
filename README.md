# FastAPI CRUD + MongoDB Atlas

API RESTful completa con FastAPI, MongoDB Atlas y mejores prácticas de desarrollo.

## 🎉 **ESTADO ACTUAL: COMPLETAMENTE FUNCIONAL**

✅ **MongoDB Atlas conectado** - Base de datos en la nube  
✅ **API ejecutándose** - http://localhost:8000  
✅ **Documentación disponible** - http://localhost:8000/docs  
✅ **Health check activo** - http://localhost:8000/health  
✅ **Todas las dependencias instaladas**  
✅ **Pydantic v2 compatible**

---

## 🚀 Características

- ✅ CRUD completo asíncrono con MongoDB Atlas
- ✅ Validación avanzada con Pydantic
- ✅ Gestión de conexiones seguras a la nube
- ✅ Manejo global de excepciones
- ✅ Logging estructurado
- ✅ Configuración por variables de entorno
- ✅ Middleware CORS configurado
- ✅ Documentación automática (Swagger/ReDoc)
- ✅ Endpoints de health check
- ✅ Paginación con límites
- ✅ Validaciones de entrada robustas
- ✅ Conexión optimizada para MongoDB Atlas

## 📁 Estructura del Proyecto

```
.
├── config.py              # Configuración de la aplicación
├── crud.py                # Operaciones CRUD
├── database.py            # Configuración de MongoDB Atlas
├── exceptions.py          # Manejo de excepciones
├── logging_config.py      # Configuración de logs
├── main.py               # Punto de entrada
├── models.py             # Modelos de datos
├── requirements.txt      # Dependencias
├── schemas.py           # Schemas de Pydantic
├── test_connection.py    # Script de prueba de conexión
├── routers/
│   └── items.py         # Rutas de la API
├── logs/               # Archivos de log (se crea automáticamente)
├── .env                # Variables de entorno (YA CONFIGURADO)
├── .env.example        # Variables de entorno de ejemplo
└── README.md          # Este archivo
```

## 🔧 Instalación y Configuración

### 1. Instalar Python
Asegúrate de tener Python 3.8+ instalado. Puedes descargarlo desde https://python.org

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. ✅ Base de Datos Configurada
**¡MongoDB Atlas ya está configurado!** 
- URL de conexión: `mongodb+srv://cluster0.nsx1xav.mongodb.net/`
- Base de datos: `fastapi_db`
- Variables de entorno ya están en `.env`

### 5. Probar conexión (opcional)

```bash
python test_connection.py
```

## 🚀 Ejecutar la Aplicación

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**¡La aplicación estará disponible en:**
- API: http://localhost:8000/api/v1/items/
- Documentación: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## 📚 Endpoints de la API

### Base URL: `http://localhost:8000/api/v1`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Health check básico |
| GET | `/health` | Health check detallado |
| POST | `/items/` | Crear item |
| GET | `/items/` | Listar items (paginado) |
| GET | `/items/{id}` | Obtener item por ID |
| PUT | `/items/{id}` | Actualizar item |
| DELETE | `/items/{id}` | Eliminar item |
| GET | `/items/stats/count` | Contar total de items |

### Documentación Interactiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔍 Ejemplos de Uso

### Crear un item
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Mi Item", "description": "Descripción del item"}'
```

### Listar items con paginación
```bash
curl "http://localhost:8000/api/v1/items/?skip=0&limit=5"
```

### Actualizar un item
```bash
curl -X PUT "http://localhost:8000/api/v1/items/{id}" \
  -H "Content-Type: application/json" \
  -d '{"name": "Nombre actualizado"}'
```

## ⚙️ Configuración MongoDB Atlas

### Variables de Entorno (.env) - ✅ YA CONFIGURADAS

```env
# MongoDB Atlas - Configuración en la nube
MONGODB_URL=mongodb+srv://shenryvladimil:ofuvzitMI9psOBrB@cluster0.nsx1xav.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DATABASE_NAME=fastapi_db

# Configuración de la aplicación
API_TITLE=FastAPI CRUD con MongoDB Atlas
API_DESCRIPTION=API RESTful para gestión de items
API_VERSION=1.0.0

# CORS y paginación
ALLOWED_ORIGINS=*
DEFAULT_PAGE_SIZE=10
MAX_PAGE_SIZE=100
LOG_LEVEL=INFO
```

### Características de la conexión Atlas:
- ✅ **Conexión segura SSL/TLS**
- ✅ **Pool de conexiones optimizado** (min: 1, max: 10)
- ✅ **Timeouts configurados** para mejor rendimiento
- ✅ **Retry automático** para escrituras
- ✅ **Verificación de ping** al conectar

### Logging

Los logs se guardan en:
- **Consola**: Todos los niveles
- **Archivo**: `logs/app.log`

## 🧪 Testing

Para probar la API:

1. Ejecutar la aplicación
2. Visitar http://localhost:8000/docs
3. Usar la interfaz Swagger para probar endpoints

## 🏗️ Mejores Prácticas Implementadas

1. **Separación de responsabilidades**: Cada módulo tiene una función específica
2. **Manejo asíncrono**: Todas las operaciones de BD son async/await
3. **Validación robusta**: Pydantic con validadores personalizados
4. **Gestión de conexiones**: Conexión/desconexión correcta a MongoDB
5. **Manejo de errores**: Excepciones personalizadas y globales
6. **Configuración centralizada**: Variables de entorno y settings
7. **Logging estructurado**: Logs en archivo y consola
8. **Documentación**: Docstrings y documentación automática
9. **Tipado estático**: Type hints en todo el código
10. **Paginación segura**: Límites y validaciones

## 🚨 Producción

Para producción, considera:

1. Usar un servidor ASGI como Gunicorn + Uvicorn
2. Configurar un proxy reverso (Nginx)
3. Implementar autenticación y autorización
4. Usar MongoDB Atlas o cluster dedicado
5. Configurar monitoring y métricas
6. Implementar rate limiting
7. Usar HTTPS
8. Configurar CORS específicos

DB mongo

shenryvladimil
ofuvzitMI9psOBrB
