from bpy.props import FloatProperty, StringProperty
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

    latent_space_image_id: StringProperty(
        name='Latent Space Image Id',
        description='Id of the latent space (preferences map) and key ' +
                    'in bpy.data.images and textures',
        default='Latent_Space'
    )
