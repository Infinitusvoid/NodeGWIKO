# TODO
# based on the input you generated an json
# than you call the GWIKOSDF with argument one argruments it path to this file
# when the program ends you read the image with pillow transform it into tansor
# pass the tensor as output image

# this links are usefull
# https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes/wiki
# https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes/wiki/Tutorial-4-%E2%80%90-Hello-World-Overlay-Text

# youtube videos
# https://www.youtube.com/watch?v=RSp9_fh3JoI

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

class NodeGWIKO:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                 "local_size_x": ("INT", {
                    "default": 16, 
                    "min": 0, #Minimum value
                    "max": 256, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "local_size_y": ("INT", {
                    "default": 16, 
                    "min": 0, #Minimum value
                    "max": 256, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_image_size_width": ("INT", {
                    "default": 1024, 
                    "min": 0, #Minimum value
                    "max": 8192, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_image_size_height": ("INT", {
                    "default": 1024, 
                    "min": 0, #Minimum value
                    "max": 8192, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                 "float_uniform_data": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_x": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_y": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_z": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_fov": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_rotation_x": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_rotation_y": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_uniform_camera_rotation_z": ("FLOAT", {
                    "default": 1.0,
                    "display": "number"}),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number"}),
                "print_to_screen": (["enable", "disable"],),
                "string_glsl_source": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "dynamicPrompts": False,
                    "default": ""
                }),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "NodeGWIKO"

    def test(self, image, string_field, string_glsl_source, int_field, local_size_x, local_size_y, int_image_size_width, int_image_size_height, float_uniform_data, float_field, print_to_screen
    ,float_uniform_camera_x, float_uniform_camera_y, float_uniform_camera_z, float_uniform_camera_fov, float_uniform_camera_rotation_x, float_uniform_camera_rotation_y, float_uniform_camera_rotation_z):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        
        string_glsl_source = replace_string(replace_string(string_glsl_source, "BEGIN", "{"), "END", "}")
        
        
        
        output_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("output")
        create_folder_if_not_exists(output_folder_path)
        
        # Sample data for the JSON
        data = {
            "file_path_output": str(output_folder_path) + "\\generated_image_qullo.png",
            "image_size": {"height":int_image_size_height,"width":int_image_size_width},
            "local_size_x":local_size_x,
            "local_size_y":local_size_y,
            "source_base64":encode_to_base64(string_glsl_source),
            "variables":[["uniform_data",float_uniform_data]],
            "version":0.1,
            "city": "New York"
        }
        
        folder_json_program = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("json_program")
        create_folder_if_not_exists(folder_json_program)
        
        
        #save_json(data, "C:/Users/Cosmos/Desktop/output/json_program_generated_from_ComfyUI.json")
        path_to_json_program = str(folder_json_program) + "\json_program_generated_from_ComfyUI.json"
        save_json(data, path_to_json_program)
        
        # Example usage:
        command = "python"  # Example command
        args = ["-c", "print('Hello, world!')"]  # Example arguments
        start_process_with_args(command, args)
        
        command = str(Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO")) + "\GWIKO.exe"
        args = ["ComfyUI2", replace_slash(path_to_json_program)]
        start_process_with_args(command, args)

        print("image if of type :")
        print(type(image))
        image = pil2tensor(load_image(str(output_folder_path) + "\\generated_image_qullo.png"))

        #do some processing on the image, in this example I just invert it
        #image = 1.0 - image
        return (image,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

