import cv2
import numpy as np
from pathlib import Path

def process_image(file_content) -> np.ndarray:
    """Convierte una imagen en un vector de características."""
    nparr = np.frombuffer(file_content, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (128, 128))  # Redimensionar
    return image.flatten().astype(np.float32)

def save_image(file_content, filename: str) -> str:
    """Guarda la imagen en la carpeta estática y devuelve la ruta."""
    file_path = Path(f"app/static/{filename}")
    with open(file_path, "wb") as f:
        f.write(file_content)
    return str(file_path)
