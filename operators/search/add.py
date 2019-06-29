import bpy
from bpy.types import Operator
import numpy as np

from material_recommender.gms import cnn
from material_recommender.gms import gplvm
from material_recommender.gms import gpr


class AddFromLatentSpaceOperator(Operator):
    bl_idname = 'scene.add_from_latent_space'
    bl_label = 'Add'
    bl_description = 'Press this button to add the material at the '\
        'given coordinates to the list for previewing'

    @classmethod
    def poll(cls, context):
        return context.scene.preferences_properties.is_gpr_trained

    def execute(self, context):
        search_properties = context.scene.search_properties
        materials = search_properties.materials.collection

        coordinates = np.array([
            search_properties.x_coordinate,
            search_properties.y_coordinate
        ])

        gplvm_model = gplvm.load_from_disk()
        gpr_model = gpr.load_from_disk()

        shader_values = gplvm.predict(
            coordinates.reshape(1, 2),
            gplvm_model=gplvm_model
        )  # return size (1, 20)
        rating = gpr.predict(shader_values, gpr_model=gpr_model)  # (1, 1)
        frames = cnn.predict(shader_values)

        materials.add()
        current_material = materials[-1]

        current_material.id = search_properties.next_id

        current_material.load_from_memory(frames)

        current_material.rating = int(np.clip(rating, 0, 10))
        current_material.shader_values = shader_values[0]

        # Generating new render of latent space
        threshold = int(context.scene.preferences_properties.threshold)
        x_above_treshold = gpr.above_threshold_x_from_model(
            threshold,
            gpr_model
        )

        pref_map = gplvm.generate_preference_map(
            x_above_treshold,
            highlight_coords=coordinates,
            gplvm_model=gplvm_model,
            gpr_model=gpr_model
        )

        height, width, _ = pref_map.shape
        alpha_channel = np.full((height, width, 1), 255)
        pref_map = np.concatenate((pref_map, alpha_channel), axis=2)

        pref_map_image_id = search_properties.latent_space_image_id
        pref_map_image = bpy.data.images[pref_map_image_id]
        pref_map_texture = bpy.data.textures[pref_map_image_id]

        # the image must be flattened because that's how blender expects it
        # also the values must be in [0, 1] interval
        # also blender saves it from the last row to the first
        pref_map_image.pixels = pref_map[::-1].flatten() / 255
        pref_map_texture.image = pref_map_image

        return {'FINISHED'}
