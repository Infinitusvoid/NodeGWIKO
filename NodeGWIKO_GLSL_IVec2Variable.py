class NodeGWIKO_GLSL_IVec2Variable:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {
                "dynamicPrompts": False,
                }
                ),
                "int_value_x": ("INT", {
                    "default": 0, 
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                } ),
                "int_value_y": ("INT", {
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

    def notify(self, name, int_value_x, int_value_y, text_input_before = None):
        print("text_input_before : ", text_input_before)
        if text_input_before == None:
            text_input_before = ""
            
        if name != "":
            return (text_input_before + "".join(["ivec2 ", name, " = ", "ivec2(", str(int_value_x), ", ",str(int_value_y),");\n"]),)
        else:
            return (text_input_before, )
            
            