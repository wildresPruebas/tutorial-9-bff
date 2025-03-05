from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from api.v1.routers import ingestion, orders, payments, products

app = FastAPI()

api_router = APIRouter(prefix="/v1")

api_router.include_router(ingestion.router)

@app.exception_handler(HTTPException)
async def service_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "Servicio no encontrado en el BFF", "path": request.url.path},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
