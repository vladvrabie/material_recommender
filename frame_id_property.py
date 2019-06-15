from bpy.props import StringProperty
from bpy.types import PropertyGroup


class FrameIdProperty(PropertyGroup):
    # CollectionProperty can only hold PropertyGroup
    id: StringProperty(
        name='Frame_Id',
        description='Frame id for a material.'
    )
