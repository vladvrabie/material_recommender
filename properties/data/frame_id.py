from bpy.props import StringProperty
from bpy.types import PropertyGroup


class FrameIdGroup(PropertyGroup):
    id: StringProperty(
        name='Frame_Id',
        description='Frame id for a material'
    )
