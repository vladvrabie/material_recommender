from bpy.types import Operator


class GPRLearnOperator(Operator):
    bl_idname = 'scene.gpr_learn'
    bl_label = 'Learn'
    bl_description = 'A model with your preferences will be trained using '\
        'this batch of ratings.'

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        return {'FINISHED'}
