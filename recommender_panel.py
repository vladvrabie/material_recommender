import bpy


class RecommenderPanel(bpy.types.Panel):
    bl_idname = "RECOMMENDER_PT_PANEL"
    bl_label = "Material Recommender"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        properties = context.scene.recommender_props

        first_row = self.layout.row()
        first_row.prop(properties, 'tabs', expand=True)
