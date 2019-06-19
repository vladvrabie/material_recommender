from bpy.props import FloatProperty
from bpy.types import PropertyGroup

from . base import BaseTabProperties


class SearchProperties(BaseTabProperties, PropertyGroup):

    x_coordinate: FloatProperty(
        name='X Coordinate',
        description='Move the point in the latent space above to preview ' +
                    'the coresponding material based on your preferences.',
        default=0,
        min=-2.5,
        max=2.5,
        precision=5,
        step=1
    )

    y_coordinate: FloatProperty(
        name='Y Coordinate',
        description='Move the point in the latent space above to preview ' +
                    'the coresponding material based on your preferences.',
        default=0,
        min=-2.5,
        max=2.5,
        precision=5,
        step=1
    )
