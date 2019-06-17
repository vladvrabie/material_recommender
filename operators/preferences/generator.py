from bpy.types import Operator
import random


class PreferencesListGenerator(Operator):
    bl_idname = 'scene.preferences_list_generator'
    bl_label = 'Populate preferences list'
    bl_description = 'A new set of materials will be generated for rating.'

    def execute(self, context):
        materials = context.scene.preferences_properties.materials.collection

        # TODO: generate 30-40 times...
        materials.add()
        current_material = materials[-1]

        # generate 19 random numbers (??? - maybe not necessary)
        # TODO: in theory, here I need to call the neural net
        # for rendering 1 or more frames per material
        # return values would be one or more ndarrays with frames
        # gpr_data.load_from_memory(list of frames)

        folder1 = ('C:\\Users\\vladv\\Desktop\\test\\h200\\', 'b_')
        folder2 = ('C:\\Users\\vladv\\Desktop\\test\\0_14_12__0\\', 'a_a_')
        # folder3 = ('C:\\Users\\vladv\\Desktop\\test\\18_6_40__0\\', 'b_')
        sel = random.sample((folder1, folder2), 1)[0]
        current_material.material_id = sel[1]
        current_material.load_from_folder(
            sel[0],
            frames_count=26,
            prefix=sel[1],
            extension='.png'
        )

        return {'FINISHED'}
