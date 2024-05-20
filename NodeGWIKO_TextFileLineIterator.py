import os
import torch
from PIL import Image, ImageOps
import numpy as np

class NodeGWIKO_TextFileLineIterator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {}),
                "line_index": ("INT", {"default": 0})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_line_by_index"
    CATEGORY = "NodeGWIKO"
    
    def get_line_by_index(self, file_path, line_index):
        # Read all lines from the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Wrap the index around using modulo
        line_index = line_index % len(lines)
        
        # Get the specified line and strip any surrounding whitespace
        line = lines[line_index].strip()
        
        return (line,)
