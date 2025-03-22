import faiss
import numpy as np

def create_faiss_index(dim: int):
    return faiss.IndexFlatL2(dim)

def add_to_index(index, vector):
    vector = np.expand_dims(vector, axis=0)  # Convertir en matriz 2D
    index.add(vector)
