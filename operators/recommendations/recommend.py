from bpy.types import Operator

from material_recommender.gms import cnn
from material_recommender.gms import gpr


class RecommendOperator(Operator):
    bl_idname = 'scene.recommend_materials'
    bl_label = 'Recommend'
    bl_description = 'A number of new materials will be generated '\
                     'based on your preferences'

    @classmethod
    def poll(cls, context):
        return context.scene.preferences_properties.is_gpr_trained

    def execute(self, context):
        preferences_properties = context.scene.preferences_properties

        recommended, ratings = gpr.recommend(
            at_least=10,
            min_threshold=int(preferences_properties.threshold)
        )  # (n, 20), (n, 1)

        number_of_recomm = recommended.shape[0]

        frames = cnn.predict(recommended)

        recommendations_properties = context.scene.recommendations_properties
        materials = recommendations_properties.materials.collection
        for i in range(number_of_recomm):
            materials.add()
            current_material = materials[-1]

            current_material.id = recommendations_properties.next_id

            current_material.load_from_memory(frames[i * 25:(i + 1) * 25])

            current_material.rating = ratings[i, 0]
            current_material.shader_values = recommended[i]

        return {'FINISHED'}
