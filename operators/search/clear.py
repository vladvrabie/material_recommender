from bpy.types import Operator


class ClearSearchesOperator(Operator):
    bl_idname = 'scene.clear_searches'
    bl_label = 'Clear'
    bl_description = 'The list of searched materials will be emptied '\
        'with the exception of the latent space'

    @classmethod
    def poll(cls, context):
        search_properties = context.scene.search_properties
        return len(search_properties.materials.collection) > 1

    def execute(self, context):
        materials = context.scene.search_properties.materials

        for i in range(len(materials.collection) - 1, 0, -1):
            materials.collection[i].clear_from_memory()
            materials.collection.remove(i)

        materials.index = 0
        return {'FINISHED'}
