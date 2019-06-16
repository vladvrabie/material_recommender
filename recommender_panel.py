from bpy.types import Panel
import random


class RecommenderPanel(Panel):
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

        gpr_materials = context.scene.gpr_materials
        row = self.layout.row()
        row.template_list(
            'GPRUIList',    # subclass of UIList
            'GPR_UI_List',  # id of widget
            gpr_materials,  # propertygroup where the collection of items is
            'mat_list',     # collection property in property group
            gpr_materials,  # propertygroup with the index of the selected item
            'index'         # index property in property group
        )

        properties = context.scene.recommender_props

        if gpr_materials.index != -1:
            row = self.layout.row()
            row.alignment = 'CENTER'
            if properties.dirty_preview is True:
                # changing scale to force a redraw on the preview
                row.scale_x = 1.0 - random.uniform(0.0, 0.1)
                row.scale_y = 1.0 + random.uniform(0.0, 0.1)
                properties.dirty_preview = False

            row.template_preview(
                gpr_materials.selected.current_frame_texture,
                show_buttons=False
            )

            row = self.layout.row()
            split_20_80 = row.split(factor=0.2)
            split_20_80.row()  # 20% to the left empty
            split_60_20 = split_20_80.split(factor=0.75)  # 60% center
            steppers_row = split_60_20.row(align=True)
            steppers_row.alignment = 'CENTER'
            steppers_row.operator('preview.previousstepper', icon='FRAME_PREV')
            steppers_row.operator('preview.nextstepper', icon='FRAME_NEXT')
            to_vse_row = split_60_20.row()  # 20% to the right
            to_vse_row.alignment = 'RIGHT'
            to_vse_row.operator('scene.export_to_vse', icon='SEQUENCE')

        row = self.layout.row()
        row.prop(properties, 'persistent_gpr')

        row = self.layout.row()
        row.operator('scene.gpr_learn')

    def _draw_recommendations_tab(self, context):
        pass
