import bpy
from bpy.types import Operator


class ExportToMaterialsOperator(Operator):
    bl_idname = 'preview.export_to_materials'
    bl_label = ''
    bl_description = 'This preview will be saved as a material based on '\
                     'a "Uber" material with a specific shader. The Uber '\
                     'material will be generated if it doesn\'t exist'

    def execute(self, context):
        # TODO: implement export to materials

        properties = context.scene.global_properties

        if properties.tabs == 'PREFERENCES':
            properties = context.scene.preferences_properties
        elif properties.tabs == 'RECOMMENDATIONS':
            properties = context.scene.recommendations_properties
        elif properties.tabs == 'SEARCH':
            properties = context.scene.search_properties

        material_data = properties.materials.selected

        uber_mat_name = 'Uber'
        uber_material = None
        if bpy.data.materials.get(uber_mat_name) is not None:
            uber_material = bpy.data.materials[uber_mat_name]
            print('found')
        else:
            uber_material = self._create_uber_material(context)
            print('created')

        return {'FINISHED'}

    def _create_uber_material(self, context):
        uber_material = bpy.data.materials.new('Uber')
        return uber_material
