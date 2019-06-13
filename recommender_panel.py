import bpy

class RecommenderPanel(bpy.types.Panel):
    bl_idname = "RECOMMENDER_PT_PANEL"
    bl_label = "Material Recommender"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        self.layout.operator("material.generate_button", text="Generate materials")
        #TODO: self.layout.operator("material.reset_button", text="Reset")
