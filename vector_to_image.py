import json
import numpy as np
from PIL import Image


def reshape_array(array):
    list_r, list_g, list_b = np.array_split(array, 3)
    rgb = list(zip(list_r, list_g, list_b))
    n = 32
    x = [rgb[i:i + n] for i in range(0, len(rgb), n)]
    return x


def vector_to_image(file):
    with open(file) as f:
        d = json.load(f)
    a = reshape_array(d)
    image_data = np.array(a, dtype=np.uint8)
    image = Image.fromarray(image_data)
    image.save('image.png')


vector_to_image(file='picture.json')
