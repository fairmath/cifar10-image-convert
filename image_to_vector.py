import json
from PIL import Image
import numpy as np


def convert_to_json(path):
    image = Image.open(path)
    image = image.convert('RGB')
    image_data = np.array(image)

    list_r = image_data[:, :, 0].tolist()  # Red channel
    list_g = image_data[:, :, 1].tolist()  # Green channel
    list_b = image_data[:, :, 2].tolist()  # Blue channel

    flat_list_r = [item for sublist in list_r for item in sublist]
    flat_list_g = [item for sublist in list_g for item in sublist]
    flat_list_b = [item for sublist in list_b for item in sublist]

    result = flat_list_r + flat_list_g + flat_list_b
    with open('image.json', 'w') as fout:
        json.dump(result, fout)


convert_to_json('image.png')
