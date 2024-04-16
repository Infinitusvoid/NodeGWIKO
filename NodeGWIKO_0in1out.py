from pathlib import Path

import os
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import base64

import comfy.utils
from torchvision import transforms

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

def start_process_with_args(command, args, no_printing):
    try:
        # Start the process with the given command and arguments
        process = subprocess.Popen([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for the process to finish and get its output
        stdout, stderr = process.communicate()
        
        # Decode output bytes to strings
        stdout_str = stdout.decode('utf-8')
        stderr_str = stderr.decode('utf-8')
        
        if no_printing:
            pass
        else:
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

def tensorToPngImage(image, filepath):
    print("tensorToPngImage")
    #print(image_input_0)
    print(image.size())
    assert image.dim() == 4 # "Tensor must be 4-dimensional"
    assert image.size(0) == 1 # "First dimension must be 1"
    #assert image_input_0.size(1) == 1024 # "Second dimension must be 1024"
    #assert image_input_0.size(2) == 1024 # "Third dimension must be 1024"
    #assert image_input_0.size(3) == 3 # "Fourth dimension must be 3"
        
    #save_tensor_as_png(image_input_0, "NodeGWIKO_pil_image_saved.png")
    #save_tensor_as_image(image_input_0, "NodeGWIKO_pil_image_saved_torch_function.png")
    
    i = 255. * image.cpu().numpy()
    #print(i)
    #print("shape", i.shape)
    
    # Reshape the array
    
    reshaped_array = i.reshape(image.size(1), image.size(2), image.size(3))
    #print("reshaped_array.shape", reshaped_array.shape)
    
    reshaped_array = np.uint8(reshaped_array)
    
    # Convert to PIL Image
    image = Image.fromarray(reshaped_array)
    
    # Save as PNG
    image.save(filepath)

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):  # Check if the file exists
        os.remove(file_path)        # Delete the file
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} does not exist.")

def read_string_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            string_data = file.read()
        return string_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

class NodeGWIKO_0in1out:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        example_shader = """
void main()
{
    ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);
    vec4 color = vec4(pixel_coords.x / 1024.0, pixel_coords.y / 1024.0, 0.0, 1.0);
    color.g = color.g + float(int_frame) * 0.01;
    imageStore(out0, pixel_coords, color);
}
"""

        return {
            "required": {
                "int_image_width": ("INT", {
                    "default": 1024,
                    "max": 16384,
                    "min": 0, #Minimum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_image_height": ("INT", {
                    "default": 1024,
                    "max": 16384,
                    "min": 0, #Minimum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_frame": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_local_size_x": ("INT", {
                    "default": 16, 
                    "min": 0, #Minimum value
                    "max": 256, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_local_size_y": ("INT", {
                    "default": 16, 
                    "min": 0, #Minimum value
                    "max": 256, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "print_to_screen": (["enable", "disable"],),
                "string_glsl_source": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "dynamicPrompts": False,
                    "default": example_shader
                    
                }),
            },
        }
    
    RETURN_TYPES = ("IMAGE", )
    #RETURN_NAMES = ("image_output_name",)
    RETURN_NAMES = ("out0", )
    
    FUNCTION = "test"
    
    #OUTPUT_NODE = False

    CATEGORY = "NodeGWIKO"
    
    def test(self, int_image_width, int_image_height, int_frame, int_local_size_x, int_local_size_y, string_glsl_source, print_to_screen):
        
        # we make sure folders we will need exist
        tmp_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp")
        create_folder_if_not_exists(tmp_folder_path)
        
        output_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp").joinpath("output")
        create_folder_if_not_exists(output_folder_path)
        
        input_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp").joinpath("input")
        create_folder_if_not_exists(input_folder_path)
        
        # delete things 

        #will have to be calculated based on root directory of project the paths should be absolute
        
        
        
        # we clear the output folder if generation fails we will know instead use previusly generated image
        
        #will have to be generated on call form torch_tensors
        input_images_list = []
        
        number_of_output_images = 1 # this is constant per node as we can't have nodes with variable number of arguments ( well maybe with batches would go but kind don't like it )
        
        # the string source could be augumeted by build in variables like frame
        string_source = "int int_frame = " +  str(int_frame) + ";\n" + string_glsl_source
        string_source = encode_to_base64(string_source)
        
        
        data = {
            "type" : "NodeGWIKO",
            "version" : "0.1",
	        "width":int_image_width,
            "height":int_image_height,
            "local_size":{"x":int_local_size_x, "y":int_local_size_y},
            "input_folder": str(input_folder_path) + "\\",
            "output_folder": str(output_folder_path) + "\\",
            "images_input": input_images_list,
            "num_images_out":number_of_output_images,
            "source" : string_source,
        }
        
        path_to_program = str(input_folder_path) + "/program.json"
        save_json(data, path_to_program)
        
        delete_file_if_exists(str(output_folder_path) + "\\out_0.png")
        delete_file_if_exists(str(output_folder_path) + "\\generated_shader.glsl.png")
        delete_file_if_exists(str(output_folder_path) + "\\log.txt")
        
        exe_file_name = "NodeGWIKO4.exe";
        command = str(Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO")) + "\\" + exe_file_name
        args = ["ComfyUI", replace_slash(path_to_program)]
        
        start_process_with_args(command, args, (print_to_screen == "disable"))
        
        image_out_0 = pil2tensor(load_image(str(output_folder_path) + "\\out_0.png"))
        
        
        if print_to_screen == "enable":
            string_of_glsl_code = read_string_from_file(str(output_folder_path) + "\\generated_shader.glsl")
            print(string_of_glsl_code)
            logging_txt = read_string_from_file(str(output_folder_path) + "\\log.txt")
            print(logging_txt)
        
        return (image_out_0, )
        