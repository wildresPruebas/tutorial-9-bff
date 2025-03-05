import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    "INGESTION_PATH": os.getenv("INGESTION_PATH", "http://users:8000"),
    "CANONIZACON_PATH": os.getenv("CANONIZACON_PATH", "http://orders:8000"),
    "ANONIMIZACION_PATH": os.getenv("ANONIMIZACION_PATH", "http://payments:8000"),
    "AUDITORIA_PATH": os.getenv("AUDITORIA_PATH", "http://products:8000"),
}
