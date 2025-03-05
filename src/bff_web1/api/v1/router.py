from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.v1.routers import ingestion, orders, payments, products

app = FastAPI()

# Router principal con prefijo global `/v1`
api_router = APIRouter(prefix="/v1")

# Agregar subrouters que ya tienen sus propios prefijos
api_router.include_router(ingestion.router)  # Maneja `/v1/users`

# Incluir el router principal en la aplicación
app.include_router(api_router)

# Manejo de errores para endpoints inexistentes
@app.exception_handler(HTTPException)
async def service_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "Endpoint not found", "path": request.url.path},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
