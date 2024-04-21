class NodeGWIKO_GLSL_Vec4Variable:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {
                "dynamicPrompts": False,
                }
                ),
                "float_value_x": ("FLOAT", {
                    "default": 0, 
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                } ),
                "float_value_y": ("FLOAT", {
                    "default": 0, 
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                } ),
                "float_value_z": ("FLOAT", {
                    "default": 0, 
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                } ),
                "float_value_w": ("FLOAT", {
                    "default": 0, 
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                } ),
            },
            "optional":{
                "text_input_before": ("STRING", {
                #"multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                "dynamicPrompts": False,
                "forceInput": True,
                "default" : "",
                }
                ),
            },
        }
    

    #INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    #OUTPUT_IS_LIST = (True,)

    CATEGORY = "NodeGWIKO"

    def notify(self, name, float_value_x, float_value_y, float_value_z, float_value_w, text_input_before = None):
        print("text_input_before : ", text_input_before)
        if text_input_before == None:
            text_input_before = ""
            
        if name != "":
            return (text_input_before + "".join(["vec4 ", name, " = ", "vec4(", str(float_value_x), ", ",str(float_value_y),", ", str(float_value_z), ", ", str(float_value_w), ");\n"]),)
        else:
            return (text_input_before, )
            
            