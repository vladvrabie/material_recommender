import numpy as np

from bpy.types import Operator

from material_recommender.gms import cnn


class PreferencesListGenerator(Operator):
    bl_idname = 'scene.preferences_list_generator'  # TODO: rename all bl_idnames
    bl_label = 'Populate preferences list'
    bl_description = 'A new set of materials will be generated for rating.'

    def execute(self, context):
        materials = context.scene.preferences_properties.materials.collection
        number_of_samples = 30

        for _ in range(number_of_samples):
            materials.add()
            current_material = materials[-1]

            # TODO: generate unique id

            current_material.shader_values = np.random.rand(20)
            current_material.shader_values[3] = 1.0

            # TODO: call the neural net
            # frames = cnn.predict(current_material.shader_values)  # frames.shape = (25, 200, 200, 3)
            # current_material.load_from_memory(frames)
            cnn.hardcoded_predict(current_material)

        return {'FINISHED'}
