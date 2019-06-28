from bpy.types import Operator

from material_recommender.gms import cnn
from material_recommender.gms import gpr


class PreferencesListGenerator(Operator):
    bl_idname = 'scene.preferences_list_generator'  # TODO: rename all bl_idnames
    bl_label = 'Populate preferences list'
    bl_description = 'A new set of materials will be generated for rating.'

    def execute(self, context):
        materials = context.scene.preferences_properties.materials.collection
        number_of_samples = 30

        shaders_values = gpr.generate_random_shader(number_of_samples)

        # TODO: call the neural net
        # frames = cnn.predict(shaders_values)  # (30*25, 120000)

        for i in range(number_of_samples):
            materials.add()
            current_material = materials[-1]

            # TODO: generate unique id

            # current_material.load_from_memory(frames)
            cnn.hardcoded_predict(current_material)

            current_material.shader_values = shaders_values[i]

        return {'FINISHED'}
