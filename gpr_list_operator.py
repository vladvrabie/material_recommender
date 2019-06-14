import bpy
from bpy.types import Operator


class GRPListGenerator(Operator):
    bl_idname = 'scene.gpr_list_generator'
    bl_label = 'Populate GPR list'

    def execute(self, context):
        gpr_data = context.scene.gpr_data
        gpr_data.add()
        return {'FINISHED'}
