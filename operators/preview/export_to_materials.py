import bpy
from bpy.types import Operator


class ExportToMaterialsOperator(Operator):
    bl_idname = 'preview.export_to_materials'
    bl_label = ''
    bl_description = 'This preview will be saved as a material based on '\
                     'a "Uber" material with a specific shader. The Uber '\
                     'material will be generated if it doesn\'t exist'

    def execute(self, context):
        properties = context.scene.global_properties

        if properties.tabs == 'PREFERENCES':
            properties = context.scene.preferences_properties
        elif properties.tabs == 'RECOMMENDATIONS':
            properties = context.scene.recommendations_properties
        elif properties.tabs == 'SEARCH':
            properties = context.scene.search_properties

        material_data = properties.materials.selected
        self._create_material(material_data)

        return {'FINISHED'}

    def _create_material(self, data):
        uber_material = bpy.data.materials.new(data.id)
        uber_material.use_nodes = True
        nodes = uber_material.node_tree.nodes
        nodes.clear()

        # Creating shader nodes
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

        # Creating links between nodes
        links = uber_material.node_tree.links
        links.new(glossy1.outputs[0], mix_glossies.inputs[1])
        links.new(glossy2.outputs[0], mix_glossies.inputs[2])

        links.new(glass.outputs[0], mix_lucids.inputs[1])
        links.new(translucent.outputs[0], mix_lucids.inputs[2])

        links.new(mix_glossies.outputs[0], mix_mixers.inputs[1])
        links.new(mix_lucids.outputs[0], mix_mixers.inputs[2])

        links.new(mix_mixers.outputs[0], material_output.inputs[0])
        links.new(volume_abs.outputs[0], material_output.inputs[1])

        # Setting input values of the nodes
        glossy1.inputs[0].default_value = (  # RGB: [0], [1], [2], 1.0
            data.shader_values[0],
            data.shader_values[1],
            data.shader_values[2],
            1.0
        )
        glossy1.inputs[1].default_value = data.shader_values[3]

        glossy2.inputs[0].default_value = (  # [4], [5], [6], 1.0
            data.shader_values[4],
            data.shader_values[5],
            data.shader_values[6],
            1.0
        )
        glossy2.inputs[1].default_value = data.shader_values[7]

        mix_glossies.inputs[0].default_value = data.shader_values[8]
        mix_lucids.inputs[0].default_value = data.shader_values[9]
        mix_mixers.inputs[0].default_value = data.shader_values[10]

        volume_abs.inputs[1].default_value = data.shader_values[11]

        glass.inputs[0].default_value = (  # [12], [13], [14], 1.0
            data.shader_values[12],
            data.shader_values[13],
            data.shader_values[14],
            1.0
        )
        glass.inputs[1].default_value = data.shader_values[15]
        glass.inputs[2].default_value = data.shader_values[16]

        translucent.inputs[0].default_value = (  # [17], [18], [19], 1.0
            data.shader_values[17],
            data.shader_values[18],
            data.shader_values[19],
            1.0
        )

        return uber_material
