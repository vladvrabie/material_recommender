from bpy.props import CollectionProperty, IntProperty
from bpy.types import PropertyGroup
from . gpr_material_data import GPRMaterialData


def index_changed(self, context):
    context.scene.recommender_props.dirty_preview = True


class GPRMaterialsList(PropertyGroup):

    mat_list: CollectionProperty(
        type=GPRMaterialData,
        name='GPR Materials List',
        description='This holds all the materials for the GPR algorithm.'
    )

    index: IntProperty(
        name='GPR Materials List Index',
        description='This will remember which material was clicked ' +
                    'by the user (for preview).',
        default=-1,
        update=index_changed
    )

    @property
    def selected(self):
        if self.index != -1:
            return self.mat_list[self.index]
