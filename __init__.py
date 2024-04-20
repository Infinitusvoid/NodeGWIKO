from .NodeGWIKO_4in4out import NodeGWIKO_4in4out
from .NodeGWIKO_0in4out import NodeGWIKO_0in4out
from .NodeGWIKO_1in1out import NodeGWIKO_1in1out
from .NodeGWIKO_0in1out import NodeGWIKO_0in1out
from .NodeGWIKO_GLSL_TextString import NodeGWIKO_GLSL_TextString

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "NodeGWIKO_4in4out":NodeGWIKO_4in4out,
    "NodeGWIKO_0in4out":NodeGWIKO_0in4out,
    "NodeGWIKO_1in1out":NodeGWIKO_1in1out,
    "NodeGWIKO_0in1out":NodeGWIKO_0in1out,
    "NodeGWIKO_GLSL_TextString":NodeGWIKO_GLSL_TextString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "NodeGWIKO_4in4out":"NodeGWIKO_4in4out 4 in 4 out",
    "NodeGWIKO_0in4out":"NodeGWIKO_0in4out 0 in 4 out",
    "NodeGWIKO_1in1out":"NodeGWIKO_1in1out 1 in 1 out",
    "NodeGWIKO_0in1out" : "NodeGWIKO_0in1out 0 in 1 out",
    "NodeGWIKO_GLSL_TextString": "NodeGWIKO GLSL TextString"
}
