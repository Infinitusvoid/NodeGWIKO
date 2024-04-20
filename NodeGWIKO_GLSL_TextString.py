class NodeGWIKO_GLSL_TextString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input_0": ("STRING", {
                "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                "dynamicPrompts": False,}
                ),
            },
            "optional":{
                "text_input_before": ("STRING", {
                "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
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

    def notify(self, text_input_0, text_input_before = None):
        print("text_input_before : ", text_input_before)
        if text_input_before == None:
            text_input_before = ""
        return (text_input_before + text_input_0,)