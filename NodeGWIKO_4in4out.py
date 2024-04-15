from pathlib import Path

import os
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import base64

def replace_string(main_string, target, replacement):
    """
    Replace all occurrences of 'target' in 'main_string' with 'replacement'.
    
    Parameters:
    main_string (str): The original string.
    target (str): The string to be replaced.
    replacement (str): The string to replace 'target' with.
    
    Returns:
    str: The modified string with replacements.
    """
    return main_string.replace(target, replacement)

def create_folder_if_not_exists(folder_path):
    """
    Creates a folder if it doesn't exist already.

    Args:
    - folder_path (str): The path of the folder to be created.

    Returns:
    - None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def encode_to_base64(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')
    
    # Encode the bytes to base64
    encoded_bytes = base64.b64encode(input_bytes)
    
    # Convert the encoded bytes back to a string
    encoded_string = encoded_bytes.decode('utf-8')
    
    return encoded_string

# Function to save JSON to a file
def save_json(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("JSON data saved to:", file_path)

def start_process_with_args(command, args):
    try:
        # Start the process with the given command and arguments
        process = subprocess.Popen([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for the process to finish and get its output
        stdout, stderr = process.communicate()
        
        # Decode output bytes to strings
        stdout_str = stdout.decode('utf-8')
        stderr_str = stderr.decode('utf-8')
        
        # Check if there's any error output
        if stderr_str:
            print("Error occurred:", stderr_str)
        else:
            print("Process output:", stdout_str)
    
    except Exception as e:
        print("An error occurred:", str(e))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def load_image(image_path):
    try:
        img = Image.open(image_path)
        print("Image loaded successfully.")
        return img
    except FileNotFoundError:
        print("Error: Image file not found.")
        return None
    except Exception as e:
        print(f"Error: Failed to load image - {str(e)}")
        return None

def replace_slash(input_string):
    return input_string.replace("/", "\\")

class NodeGWIKO_4in4out:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_input_0": ("IMAGE",),
                "image_input_1": ("IMAGE",),
                "image_input_2": ("IMAGE",),
                "image_input_3": ("IMAGE",),
                "int_frame": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "print_to_screen": (["enable", "disable"],),
                "string_glsl_source": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "dynamicPrompts": False,
                    "default": "void main{}"
                }),
            },
        }
    
    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)
    
    FUNCTION = "test"
    
    #OUTPUT_NODE = False

    CATEGORY = "NodeGWIKO"
    
    def test(self, image_input_0, image_input_1, image_input_2, image_input_3, int_frame, print_to_screen, string_glsl_source):
        pass