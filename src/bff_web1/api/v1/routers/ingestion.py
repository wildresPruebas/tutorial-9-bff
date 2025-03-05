from fastapi import APIRouter
from app.v1.config import settings
from app.v1.services.external_api import fetch_data, send_data

router = APIRouter(prefix="/ingestion")

INGESTION_PATH = settings["INGESTION_PATH"]

@router.get("/")
def get_users():
    return fetch_data(f"{INGESTION_PATH}/ingestion")

@router.post("/")
def create_user(user: dict):
    return send_data(f"{INGESTION_PATH}/ingestion", user)