from bpy.types import Operator


class LearnPreferencesOperator(Operator):
    bl_idname = 'scene.learn_preferences'
    bl_label = 'Learn'
    bl_description = 'A model with your preferences will be trained using '\
        'this batch of ratings.'

    @classmethod
    def poll(cls, context):
        # TODO: if at least one is different than 0
        return True

    def execute(self, context):
        # TODO: implement learn operator
        return {'FINISHED'}
