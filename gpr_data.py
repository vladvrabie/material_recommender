import bpy
from bpy.props import IntProperty, FloatVectorProperty, StringProperty
from bpy.types import PropertyGroup


class GPRData(PropertyGroup):

    values: FloatVectorProperty(
        name='Values',
        description='Values for shader',
        size=19,
        precision=8
    )

    rating: IntProperty(
        name='Rating',
        description='The rating given for a specific material. If given a high rating, ' +
            'similar materials will be recommended.',
        default=0,
        min=0,
        max=10
    )

    image_id: StringProperty(
        name='Image_Id',
        description='The id of the image to be found in bpy.data.images',
    )
