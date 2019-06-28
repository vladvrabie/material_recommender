from bpy.types import Operator


class ClearRecommendationsOperator(Operator):
    bl_idname = 'scene.clear_recommendations'
    bl_label = 'Clear'
    bl_description = 'The list of recommended materials will be emptied'

    @classmethod
    def poll(cls, context):
        recommendations_properties = context.scene.recommendations_properties
        return len(recommendations_properties.materials.collection) != 0

    def execute(self, context):
        materials = context.scene.recommendations_properties.materials
        for material in materials.collection:
            material.clear_from_memory()
        materials.collection.clear()
        materials.index = -1
        return {'FINISHED'}
