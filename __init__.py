from .NodeGWIKO import NodeGWIKO
from .NodeGWIKO_4in4out import NodeGWIKO_4in4out
from .NodeGWIKO_0in4out import NodeGWIKO_0in4out
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "NodeGWIKO": NodeGWIKO,
    "NodeGWIKO_4in4out":NodeGWIKO_4in4out,
    "NodeGWIKO_0in4out":NodeGWIKO_0in4out
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "NodeGWIKO": "NodeGWIKO Node",
    "NodeGWIKO_4in4out":"NodeGWIKO_4in4out 4 in 4 out",
    "NodeGWIKO_0in4out":"NodeGWIKO_0in4out 0 in 4 out"
}
