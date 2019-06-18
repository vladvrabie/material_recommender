import bpy
from bpy.props import BoolProperty, FloatProperty, StringProperty
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
        description='Id of the latent space image by which to identify it ' +
                    'in bpy.data.images and textures',
        default='latent_space_image'
    )

    latent_space_dirty_preview: BoolProperty(
        name='Is Latent Space Preview Dirty',
        description='This toggles when a new latent space is generated ' +
                    'by the preferences tab, which will cause a redraw.',
        default=False
    )

    @property
    def latent_space_texture(self):
        if self.latent_space_image_id in bpy.data.textures:
            return bpy.data.textures[self.latent_space_image_id]
