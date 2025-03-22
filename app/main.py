from fastapi import FastAPI
from app.routes import router
from app.config import STATIC_DIR
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Incluir rutas
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
