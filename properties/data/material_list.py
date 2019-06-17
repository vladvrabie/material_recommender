from bpy.props import CollectionProperty, IntProperty
from bpy.types import PropertyGroup

from . material_data import MaterialData


def index_changed(self, context):
    properties = context.scene.global_properties

    if properties.tabs == 'PREFERENCES':
        context.scene.preferences_properties.dirty_preview = True
    elif properties.tabs == 'RECOMMENDATIONS':
        context.scene.recommendations_properties.dirty_preview = True


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
            return self.collection[self.index]
