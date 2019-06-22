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
        uber_material.use_nodes = True
        nodes = uber_material.node_tree.nodes
        nodes.clear()

        glossy_bsdf_id = 'ShaderNodeBsdfGlossy'
        glossy1 = nodes.new(glossy_bsdf_id)
        glossy1.name = 'Glossy1 BSDF'
        glossy1.location = (-130.0, 340.0)

        glossy2 = nodes.new(glossy_bsdf_id)
        glossy2.name = 'Glossy2 BSDF'
        glossy2.location = (-130.0, 180.0)

        glass_bsdf_id = 'ShaderNodeBsdfGlass'
        glass = nodes.new(glass_bsdf_id)
        glass.name = 'Glass BSDF'
        glass.location = (-130.0, 20.0)

        translucent_bsdf_id = 'ShaderNodeBsdfTranslucent'
        translucent = nodes.new(translucent_bsdf_id)
        translucent.name = 'Translucent BSDF'
        translucent.location = (-130.0, -160.0)

        mix_id = 'ShaderNodeMixShader'
        mix_glossies = nodes.new(mix_id)
        mix_glossies.name = 'Mix Glossies Shader'
        mix_glossies.location = (200.0, 250.0)

        mix_lucids = nodes.new(mix_id)
        mix_lucids.name = 'Mix Lucids Shader'
        mix_lucids.location = (200.0, -10.0)

        mix_mixers = nodes.new(mix_id)
        mix_mixers.name = 'Mix Mixers Shader'
        mix_mixers.location = (500.0, 150.0)

        volume_abs_id = 'ShaderNodeVolumeAbsorption'
        volume_abs = nodes.new(volume_abs_id)
        volume_abs.name = 'Volume Absorbtion Shader'
        volume_abs.location = (500.0, 0.0)

        material_output_id = 'ShaderNodeOutputMaterial'
        material_output = nodes.new(material_output_id)
        material_output.name = 'Material Output'
        material_output.location = (800.0, 60.0)

        return uber_material
