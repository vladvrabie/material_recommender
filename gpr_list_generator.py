from bpy.types import Operator
import random


class GRPListGenerator(Operator):
    bl_idname = 'scene.gpr_list_generator'
    bl_label = 'Populate GPR list'
    bl_description = 'A new set of materials will be generated for rating.'

    def execute(self, context):
        gpr_materials = context.scene.gpr_materials.mat_list

        # 30-40 times...
        gpr_materials.add()
        current_material = gpr_materials[-1]

        # generate 19 random numbers (??? - maybe not necessary)
        # TODO: in theory, here I need to call the neural net
        # for rendering 1 or more frames per material
        # return values would be one or more ndarrays with frames
        # gpr_data.load_from_memory(list of frames)

        # folder2 = ('C:\\Users\\vladv\\Desktop\\test\\18_1_7__0\\', 'a_')
        # folder3 = ('C:\\Users\\vladv\\Desktop\\test\\18_6_40__0\\', 'b_')
        # folder1 = ('C:\\Users\\vladv\\Desktop\\test\\h200\\', 'c_')
        # sel = random.sample((folder1, folder2, folder3), 1)[0]
        # current_material.material_id = 'test'
        current_material.load_from_folder(
            'C:\\Users\\vladv\\Desktop\\test\\h200\\',
            frames_count=26,
            prefix='',
            extension='.png'
        )

        return {'FINISHED'}
