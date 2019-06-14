import bpy
from bpy.types import Operator


class GRPListGenerator(Operator):
    bl_idname = 'scene.gpr_list_generator'
    bl_label = 'Populate GPR list'

    def execute(self, context):
        gpr_data = context.scene.gpr_data
        gpr_data.add()
        bpy.data.images.load("C:\\Users\\vladv\\Desktop\\test\\18_1_7__0\\frame0000.png")
        bpy.data.textures.new(name='frame0000.png', type='IMAGE')
        bpy.data.textures['frame0000.png'].image = bpy.data.images['frame0000.png']
        return {'FINISHED'}
