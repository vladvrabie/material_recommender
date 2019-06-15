import bpy
from bpy.props import CollectionProperty, IntProperty
from bpy.props import FloatVectorProperty, StringProperty
from bpy.types import PropertyGroup
from . frame_id_property import FrameIdProperty


class GPRMaterialData(PropertyGroup):

    material_id: StringProperty(
        name='Material_Id',
        description='Unique id for this generated material',
    )

    frames_ids: CollectionProperty(
        type=FrameIdProperty,
        name='Frames_IDs',
        description='IDs of the frames of the generated material for ' +
                    'retrieval from bpy.data images or textures.'
    )

    preview_frame_index: IntProperty(
        name='Previewed Frame Index',
        description='Remebers which frame is previewed.'
    )

    rating: IntProperty(
        name='Rating',
        description='The rating given for a specific material. If given ' +
                    'a high rating, similar materials will be recommended.',
        default=0,
        min=0,
        max=10
    )

    values: FloatVectorProperty(
        name='Values',
        description='Values for shader to render the material.',
        size=19,
        precision=8
    )

    @property
    def current_frame_texture(self):
        return self.frame_texture(self.preview_frame_index)

    def frame_texture(self, frame_index):
        ''' Utility function to get the texture of a frame. '''
        return bpy.data.textures[self.frames_ids[frame_index].id]

    def load_from_folder(self, path, frames_count=1, prefix='', extension=''):
        ''' prefix + "frame" + str(i).zfill(4) + extension '''
        for i in range(0, frames_count):
            file_name = prefix + "frame" + str(i).zfill(4) + extension
            self.frames_ids.add()
            self.frames_ids[-1].id = file_name

            bpy.data.images.load(path + file_name)
            bpy.data.textures.new(name=file_name, type='IMAGE')
            bpy.data.textures[file_name].image = bpy.data.images[file_name]

    def load_from_memory(list_of_images):
        pass
