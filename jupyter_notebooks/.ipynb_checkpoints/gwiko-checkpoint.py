import os
import base64
import importlib
import subprocess
import json

def print_yea():
    print("yea")


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


def reload_lib(lib_name):
    try:
        lib = importlib.import_module(lib_name)
        importlib.reload(lib)
        print(f"{lib_name} reloaded successfully.")
    except ImportError:
        print(f"Error: {lib_name} not found.")


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


def delete_file_if_exists(file_path):
    if os.path.exists(file_path):  # Check if the file exists
        os.remove(file_path)        # Delete the file
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} does not exist.")


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


