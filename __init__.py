from .NodeGWIKO_4in4out import NodeGWIKO_4in4out
from .NodeGWIKO_0in4out import NodeGWIKO_0in4out
from .NodeGWIKO_1in1out import NodeGWIKO_1in1out
from .NodeGWIKO_0in1out import NodeGWIKO_0in1out
from .NodeGWIKO_GLSL_TextString import NodeGWIKO_GLSL_TextString
from .NodeGWIKO_GLSL_IntVariable import NodeGWIKO_GLSL_IntVariable
from .NodeGWIKO_GLSL_FloatVariable import NodeGWIKO_GLSL_FloatVariable
from .NodeGWIKO_GLSL_Vec2Variable import NodeGWIKO_GLSL_Vec2Variable
from .NodeGWIKO_GLSL_Vec3Variable import NodeGWIKO_GLSL_Vec3Variable
from .NodeGWIKO_GLSL_Vec4Variable import NodeGWIKO_GLSL_Vec4Variable
from .NodeGWIKO_GLSL_IVec2Variable import NodeGWIKO_GLSL_IVec2Variable
from .NodeGWIKO_GLSL_IVec3Variable import NodeGWIKO_GLSL_IVec3Variable
from .NodeGWIKO_GLSL_IVec4Variable import NodeGWIKO_GLSL_IVec4Variable
from .NodeGWIKO_TextFileLineIterator import NodeGWIKO_TextFileLineIterator
from .NodeGWIKO_ImageDirIterator import NodeGWIKO_ImageDirIterator
from .NodeGWIKO_VidDirIterator import NodeGWIKO_VidDirIterator

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "NodeGWIKO_4in4out":NodeGWIKO_4in4out,
    "NodeGWIKO_0in4out":NodeGWIKO_0in4out,
    "NodeGWIKO_1in1out":NodeGWIKO_1in1out,
    "NodeGWIKO_0in1out":NodeGWIKO_0in1out,
    "NodeGWIKO_GLSL_TextString":NodeGWIKO_GLSL_TextString,
    "NodeGWIKO_GLSL_IntVariable":NodeGWIKO_GLSL_IntVariable,
    "NodeGWIKO_GLSL_FloatVariable":NodeGWIKO_GLSL_FloatVariable,
    "NodeGWIKO_GLSL_Vec2Variable":NodeGWIKO_GLSL_Vec2Variable,
    "NodeGWIKO_GLSL_Vec3Variable":NodeGWIKO_GLSL_Vec3Variable,
    "NodeGWIKO_GLSL_Vec4Variable":NodeGWIKO_GLSL_Vec4Variable,
    "NodeGWIKO_GLSL_IVec2Variable":NodeGWIKO_GLSL_IVec2Variable,
    "NodeGWIKO_GLSL_IVec3Variable":NodeGWIKO_GLSL_IVec3Variable,
    "NodeGWIKO_GLSL_IVec4Variable":NodeGWIKO_GLSL_IVec4Variable,
    "NodeGWIKO_TextFileLineIterator":NodeGWIKO_TextFileLineIterator,
    "NodeGWIKO_ImageDirIterator":NodeGWIKO_ImageDirIterator,
    "NodeGWIKO_VidDirIterator":NodeGWIKO_VidDirIterator
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "NodeGWIKO_4in4out":"NodeGWIKO_4in4out 4 in 4 out",
    "NodeGWIKO_0in4out":"NodeGWIKO_0in4out 0 in 4 out",
    "NodeGWIKO_1in1out":"NodeGWIKO_1in1out 1 in 1 out",
    "NodeGWIKO_0in1out" : "NodeGWIKO_0in1out 0 in 1 out",
    "NodeGWIKO_GLSL_TextString": "NodeGWIKO GLSL TextString",
    "NodeGWIKO_GLSL_IntVariable" : "NodeGWIKO GLSL IntVariable",
    "NodeGWIKO_GLSL_FloatVariable" : "NodeGWIKO GLSL FloatVariable",
    "NodeGWIKO_GLSL_Vec2Variable" : "NodeGWIKO GLSL Vec2Variable",
    "NodeGWIKO_GLSL_Vec3Variable" : "NodeGWIKO GLSL Vec3Variable",
    "NodeGWIKO_GLSL_Vec4Variable" : "NodeGWIKO GLSL Vec4Variable",
    "NodeGWIKO_GLSL_IVec2Variable" : "NodeGWIKO GLSL IVec2Variable",
    "NodeGWIKO_GLSL_IVec3Variable" : "NodeGWIKO GLSL IVec3Variable",
    "NodeGWIKO_GLSL_IVec4Variable" : "NodeGWIKO GLSL IVec4Variable",
    "NodeGWIKO_TextFileLineIterator" : "NodeGWIKO TextFileLineIterator",
    "NodeGWIKO_ImageDirIterator" : "NodeGWIKO ImageDirIterator",
    "NodeGWIKO_VidDirIterator" : "NodeGWIKO VidDirIterator"
}
