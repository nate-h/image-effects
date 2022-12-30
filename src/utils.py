from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2


def save_gray(garr: np.ndarray, name: str):
    """Saves a 2D grayscale image."""
    image2 = Image.fromarray(np.uint8(garr), "L")
    os.makedirs("generated", exist_ok=True)
    image2.save(f"generated/{name}")


def adjust_gamma(image: np.ndarray, gamma=1.0):
    """Adjust an image's gamma using a look up table."""
    invGamma = 1.0 / gamma
    float_table = [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    table = np.array(float_table).astype("uint8")
    return cv2.LUT(image, table)
