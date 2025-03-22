from fastapi import APIRouter, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from app.config import templates, index
from app.utils import process_image, save_image
from app.models import add_to_index

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload-image/")
async def upload_image(
    file: UploadFile = File(...),
    username: str = Form(...),
    age: int = Form(...),
    interests: str = Form(...)
):
    contents = await file.read()
    vector = process_image(contents)  # Convertir en vector

    file_path = save_image(contents, file.filename)  # Guardar imagen

    add_to_index(index, vector)  # Guardar en Faiss

    response = {
        "username": username,
        "age": age,
        "interests": interests.split(","),
        "vector_length": len(vector),
        "vector_sample": vector[:5].tolist(),
        "message": "Imagen procesada y almacenada en Faiss",
        "image_path": file_path
    }
    return response
