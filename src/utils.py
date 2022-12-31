from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2


def load_rgb(path: str):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

def plot(rows, cols, *images: tuple[str, np.ndarray], figsize: None | tuple[int, int] = None):
    """Generically plots images and their titles while removing the axis."""
    # Single image.
    if rows == cols == 1:
        plt.title(images[0][0])
        plt.imshow(images[0][1])
        plt.axis("off")
        return
    # Many images.
    f, axs = plt.subplots(rows, cols, figsize=figsize)
    for index, (title, image) in enumerate(images):
        if image.ndim == 2:
            axs[index].imshow(image, cmap="gray")
        else:
            axs[index].imshow(image)
        axs[index].axis('off')
        axs[index].title.set_text(title)
    f.tight_layout()

def save_gray(garr: np.ndarray, name: str):
    """Saves a 2D grayscale image."""
    image2 = Image.fromarray(np.uint8(garr), "L")
    os.makedirs("generated", exist_ok=True)
    image2.save(f"generated/{name}")


def adjust_exponential(image: np.ndarray, gamma=1.0):
    """Adjust an array exponentially using a look up table.

    This is a very handy function for things like gamma correction."""
    invGamma = 1.0 / gamma
    float_table = [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    table = np.array(float_table).astype("uint8")
    return cv2.LUT(image, table)
