import bpy
from bpy.types import Operator
import numpy as np

from material_recommender.gms import gpr
from material_recommender.gms import gplvm


class LearnPreferencesOperator(Operator):
    bl_idname = 'scene.learn_preferences'
    bl_label = 'Learn'
    bl_description = 'A model with your preferences will be trained using '\
        'this batch of ratings.'

    @classmethod
    def poll(cls, context):
        materials = context.scene.preferences_properties.materials.collection
        for material in materials:
            if material.rating != 0:
                return True
        return False

    def execute(self, context):
        preferences_properties = context.scene.preferences_properties

        trained_gpr = gpr.train(
            preferences_properties.materials.collection,
            preferences_properties.is_persistent
        )

        threshold = int(preferences_properties.threshold)
        x_above_treshold = gpr.above_threshold_x_from_model(
            threshold,
            trained_gpr
        )

        trained_gplvm = gplvm.train(x_above_treshold)

        pref_map = gplvm.generate_preference_map(
            x_above_treshold,
            gplvm_model=trained_gplvm,
            gpr_model=trained_gpr
        )

        search_properties = context.scene.search_properties
        pref_map_image_id = search_properties.latent_space_image_id

        if pref_map_image_id not in bpy.data.images.keys():
            pref_map_image = bpy.data.images.new(
                pref_map_image_id,
                width=pref_map.shape[1],
                height=pref_map.shape[0],
                alpha=True,
                float_buffer=False
            )
            pref_map_texture = bpy.data.textures.new(
                name=pref_map_image_id,
                type='IMAGE'
            )
            search_properties.materials.collection.add()
            search_properties.materials.index = 0
            pref_map_data = search_properties.materials.collection[0]
            pref_map_data.id = pref_map_image_id
            pref_map_data.frames_ids.add()
            pref_map_data.frames_ids[0].id = pref_map_image_id
        else:
            pref_map_image = bpy.data.images[pref_map_image_id]
            pref_map_texture = bpy.data.textures[pref_map_image_id]

        height, width, _ = pref_map.shape
        alpha_channel = np.full((height, width, 1), 255)
        pref_map = np.concatenate((pref_map, alpha_channel), axis=2)
        # the image must be flattened because that's how blender expects it
        # also blender saves it from the last row to the first
        pref_map_image.pixels = pref_map[::-1].flatten() / 255
        pref_map_texture.image = pref_map_image

        preferences_properties.is_gpr_trained = True
        return {'FINISHED'}
