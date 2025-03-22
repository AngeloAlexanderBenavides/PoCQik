from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import faiss

# 📌 Directorios
STATIC_DIR = Path("app/static")
TEMPLATES_DIR = Path("app/templates")

#Crear directorios si no existen
STATIC_DIR.mkdir(exist_ok=True, parents=True)

#Inicializar Templates y Archivos Estáticos
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

#Crear índice de Faiss
dimension = 128 * 128
index = faiss.IndexFlatL2(dimension)
