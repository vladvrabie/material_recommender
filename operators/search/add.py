import random

from bpy.types import Operator


class AddFromLatentSpaceOperator(Operator):
    bl_idname = 'scene.add_from_latent_space'
    bl_label = 'Add'
    bl_description = 'Press this button to add the material at the '\
        'given coordinates to the list for previewing'

    @classmethod
    def poll(cls, context):
        return context.scene.preferences_properties.is_gpr_trained

    def execute(self, context):
        properties = context.scene.search_properties
        materials = properties.materials.collection

        # TODO: implement add from latent space
        # get material float values from latent space
        # generate frames
        # load frames into blender and create material property group
        # MAYBE: generate new render of latent space

        # MOCK
        materials.add()
        current_material = materials[-1]
        folder1 = ('C:\\Users\\vladv\\Desktop\\test\\h200\\', 'b_')
        folder2 = ('C:\\Users\\vladv\\Desktop\\test\\0_14_12__0\\', 'a_a_')
        # folder3 = ('C:\\Users\\vladv\\Desktop\\test\\18_6_40__0\\', 'b_')
        sel = random.sample((folder1, folder2), 1)[0]
        current_material.id = sel[1]
        current_material.load_from_folder(
            sel[0],
            frames_count=26,
            prefix=sel[1],
            extension='.png'
        )
        # END MOCK

        return {'FINISHED'}
