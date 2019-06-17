from bpy.props import CollectionProperty, IntProperty
from bpy.types import PropertyGroup

from . material_data import MaterialData


def index_changed(self, context):
    context.scene.recommender_props.dirty_preview = True


class MaterialList(PropertyGroup):

    collection: CollectionProperty(
        type=MaterialData,
        name='Material List',
        description='This holds a list of materials.'
    )

    index: IntProperty(
        name='Materials List Index',
        description='This will remember which material was clicked ' +
                    'by the user (for preview).',
        default=-1,
        update=index_changed
    )

    @property
    def selected(self):
        if self.index != -1:
            return self.mat_list[self.index]
