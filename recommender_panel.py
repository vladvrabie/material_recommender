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

        if properties.tabs == 'LEARN':
            self._draw_learn_tab(context)
        elif properties.tabs == 'RECOMMENDATIONS':
            self._draw_recommendations_tab(context)
    
    def _draw_learn_tab(self, context):
        row = self.layout.row()
        row.operator('scene.gpr_list_generator')

        gpr_data = context.scene.gpr_data
        for i in range(len(gpr_data)):
            row = self.layout.row()
            split = row.split(factor=0.5)
            column1 = split.column()
            column1.template_preview(bpy.data.textures['frame0000.png'], show_buttons=False)
        
            column2 = split.column()
            column2.prop(gpr_data[i], 'rating', text='Rating', slider=True)
    
    def _draw_recommendations_tab(self, context):
        pass
