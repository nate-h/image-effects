from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os

def save_gray(garr: np.ndarray, name: str):
    image2 = Image.fromarray(np.uint8(garr), "L")
    os.makedirs("generated", exist_ok=True)
    image2.save(f"generated/{name}")