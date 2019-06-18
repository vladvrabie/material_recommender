from bpy.types import Operator


class ClearRecommendationsOperator(Operator):
    bl_idname = 'scene.clear_recommendations'
    bl_label = 'Clear'
    bl_description = 'The list of recommended materials will be emptied'

    @classmethod
    def poll(cls, context):
        return len(context.scene.recommendations_properties.materials.collection) != 0

    def execute(self, context):
        materials = context.scene.recommendations_properties.materials
        materials.collection.clear()
        materials.index = -1
        return {'FINISHED'}
