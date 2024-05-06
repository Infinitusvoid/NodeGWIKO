from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
#from torchvision import transforms

from IPython.display import display

import os
import numpy as np
import torch
import subprocess
import json


import gwiko

class Generate():
    class FolderFileIO():
        def __init__(self, folder_path):
            #tmp_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp")
            self.tmp_folder = Path(folder_path)
            gwiko.create_folder_if_not_exists(self.tmp_folder)
            
            #output_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp").joinpath("output")
            self.output_folder = Path(folder_path + "output")
            gwiko.create_folder_if_not_exists(self.output_folder)
            
            #input_folder_path = Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO").joinpath("tmp").joinpath("input")
            self.input_folder = Path(folder_path + "input")
            gwiko.create_folder_if_not_exists(self.input_folder)
        def get_path_to_program(self):
            return str(input_folder_path) + "/program.json"
    
    def __init__(self, folder_path):
        self.int_image_width = 1024
        self.int_image_height = 1024
        self.int_local_size_x = 16
        self.int_local_size_y = 16

        self.input_images_list = []
        self.number_of_output_images = 1

        self.folders = self.FolderFileIO(folder_path)
    def set_size(self, width, height):
        self.int_image_width = width
        self.int_image_height = height
    def generate(self, source, print_to_screen = True):
        source = gwiko.encode_to_base64(source)
        
        data = {
        "type": "NodeGWIKO",
        "version" : "0.1",
        "width":self.int_image_width,
        "height":self.int_image_height,
        "local_size":{"x":self.int_local_size_x, "y": self.int_local_size_y},
        "input_folder": str(self.folders.input_folder) + "\\",
        "output_folder": str(self.folders.output_folder) + "\\",
        "images_input": self.input_images_list,
        "num_images_out":self.number_of_output_images,
        "source" : source,
        }
        
        path_to_program = str(self.folders.input_folder) + "/program.json"
        gwiko.save_json(data, path_to_program);

        gwiko.delete_file_if_exists(str(self.folders.output_folder) + "\\out_0.png")
        gwiko.delete_file_if_exists(str(self.folders.output_folder) + "\\generated_shader.glsl.png")
        gwiko.delete_file_if_exists(str(self.folders.output_folder) + "\\log.txt")

        exe_file_name = "NodeGWIKO4.exe";
        #command = str(Path.cwd().joinpath("ComfyUI").joinpath("custom_nodes").joinpath("NodeGWIKO")) + "\\" + exe_file_name
        command = str(Path.cwd().parent) + "\\" + exe_file_name

        args = ["ComfyUI", gwiko.replace_slash(path_to_program)]
        response = gwiko.start_process_with_args(command, args)
        
        image_out_0_pil_image = gwiko.load_image(str(self.folders.output_folder) + "\\out_0.png")
        image_out_0_pil_image = image_out_0_pil_image.convert("RGB")
        image_out_0 = gwiko.pil2tensor(image_out_0_pil_image)
        if print_to_screen:
            string_of_glsl_code = gwiko.read_string_from_file(str(output_folder_path) + "\\generated_shader.glsl")
            print(string_of_glsl_code)
            logging_txt = gwiko.read_string_from_file(str(output_folder_path) + "\\log.txt")
            print(logging_txt)
            print(image_out_0)
            print(response)
        display(image_out_0_pil_image)