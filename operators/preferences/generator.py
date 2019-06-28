from bpy.types import Operator

from material_recommender.gms import cnn
from material_recommender.gms import gpr


class PreferencesListGenerator(Operator):
    bl_idname = 'scene.preferences_list_generator'  # TODO: rename all bl_idnames
    bl_label = 'Populate preferences list'
    bl_description = 'A new set of materials will be generated for rating.'

    def execute(self, context):
        preferences_properties = context.scene.preferences_properties
        materials = preferences_properties.materials.collection
        number_of_samples = 30

        for material in materials:
            material.clear_from_memory()
        materials.clear()

        shaders_values = gpr.generate_random_shader(number_of_samples)

        frames = cnn.predict(shaders_values)  # (30*25, 120000)

        for i in range(number_of_samples):
            materials.add()
            current_material = materials[-1]

            current_material.id = preferences_properties.next_id

            material_frames = frames[i * 25:(i + 1) * 25]
            current_material.load_from_memory(material_frames)

            current_material.shader_values = shaders_values[i]

        return {'FINISHED'}
