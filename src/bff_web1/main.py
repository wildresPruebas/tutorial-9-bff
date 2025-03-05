from fastapi import FastAPI
from api.v1.router import router

app = FastAPI(title="BFF API")

app.include_router(router, prefix="/v1")