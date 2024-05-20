import os
import torch
from PIL import Image, ImageOps
import numpy as np

class NodeGWIKO_ImageDirIterator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "directory_path": ("STRING", {}),
                "image_index": ("INT", {"default": 0})
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")

    FUNCTION = "get_image_by_index"

    CATEGORY = "NodeGWIKO"

    def get_image_by_index(self, directory_path, image_index):
        # Get list of image files sorted by modification time (most recent first)
        image_files = sorted(
            [os.path.join(directory_path, f) for f in os.listdir(directory_path)
             if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))],
            key=lambda x: os.path.getmtime(x), reverse=True
        )

        # Wrap the index around using modulo
        image_index = image_index % len(image_files)

        # Load and preprocess the image
        image = Image.open(image_files[image_index])
        image = ImageOps.exif_transpose(image)  # Correct orientation
        image = image.convert("RGB")  # Ensure image is in RGB format

        # Convert image to tensor
        image_tensor = torch.from_numpy(np.array(image).astype(np.float32) / 255.0)[None,]

        # Get the filename without extension and remove quotes
        filename_without_ext = os.path.splitext(os.path.basename(image_files[image_index]))[0]
        filename_without_ext = filename_without_ext.encode('utf-8').decode('unicode_escape')

        return (image_tensor, filename_without_ext)