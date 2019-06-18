import random

from bpy.types import Operator


class RecommendOperator(Operator):
    bl_idname = 'scene.recommend_materials'
    bl_label = 'Recommend'
    bl_description = 'A number of new materials will be generated '\
                     'based on your preferences'

    @classmethod
    def poll(cls, context):
        # TODO: if gpr was trained
        return True

    def execute(self, context):
        # TODO: implement recommend operator

        # MOCK GENERATION (to test preview)
        materials = context.scene.recommendations_properties.materials.collection
        materials.add()
        current_material = materials[-1]
        folder1 = ('C:\\Users\\vladv\\Desktop\\test\\h200\\', 'b_')
        folder2 = ('C:\\Users\\vladv\\Desktop\\test\\0_14_12__0\\', 'a_a_')
        sel = random.sample((folder1, folder2), 1)[0]
        current_material.material_id = sel[1]
        current_material.load_from_folder(
            sel[0],
            frames_count=26,
            prefix=sel[1],
            extension='.png'
        )
        # END MOCK GENERATION

        return {'FINISHED'}
