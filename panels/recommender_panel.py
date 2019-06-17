import random

from bpy.types import Panel


class RecommenderPanel(Panel):
    bl_idname = "RECOMMENDER_PT_PANEL"
    bl_label = "Material Recommender"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        properties = context.scene.global_properties

        first_row = self.layout.row()
        first_row.prop(properties, 'tabs', expand=True)

        if properties.tabs == 'PREFERENCES':
            self._draw_preferences_tab(context)
        elif properties.tabs == 'RECOMMENDATIONS':
            self._draw_recommendations_tab(context)
        elif properties.tabs == 'SEARCH':
            self._draw_search_tab(context)

    def _draw_preferences_tab(self, context):
        properties = context.scene.preferences_properties
        materials = properties.materials

        row = self.layout.row()
        row.operator('scene.preferences_list_generator')

        self._draw_template_list(
            materials,
            'PreferencesList',
            'Preferences_UI_List'
        )

        if materials.index != -1:
            self._draw_material_preview(properties)

        if len(materials.collection) > 0:
            row = self.layout.row()
            row.prop(properties, 'is_persistent')

            row = self.layout.row()
            row.prop(properties, 'threshold', slider=True)

            row = self.layout.row()
            row.operator('scene.learn_preferences')

    def _draw_recommendations_tab(self, context):
        # TODO: draw recommendations tab
        pass

    def _draw_search_tab(self, context):
        # TODO: draw search tab
        pass

    def _draw_template_list(self, materials, subclass, id):
        row = self.layout.row()
        row.template_list(
            subclass,       # subclass of UIList
            id,             # id of widget
            materials,      # propertygroup where the collection of items is
            'collection',   # collection property in property group
            materials,      # propertygroup with the index of the selected item
            'index'         # index property in property group
        )

    def _draw_material_preview(self, properties):
        materials = properties.materials

        row = self.layout.row()
        row.alignment = 'CENTER'
        if properties.dirty_preview is True:
            # changing scale to force a redraw on the preview
            row.scale_x = 1.0 - random.uniform(0.0, 0.1)
            row.scale_y = 1.0 + random.uniform(0.0, 0.1)
            properties.dirty_preview = False

        row.template_preview(
            materials.selected.current_frame_texture,
            show_buttons=False
        )

        row = self.layout.row()
        split_20_80 = row.split(factor=0.2)
        row = split_20_80.row()  # 20% to the left
        row.alignment = 'LEFT'
        row.operator('preview.export_to_materials', icon='MATERIAL')

        split_60_20 = split_20_80.split(factor=0.75)  # 60% center
        steppers_row = split_60_20.row(align=True)
        steppers_row.alignment = 'CENTER'
        steppers_row.operator('preview.previous_stepper', icon='FRAME_PREV')
        steppers_row.operator('preview.next_stepper', icon='FRAME_NEXT')

        to_vse_row = split_60_20.row()  # 20% to the right
        to_vse_row.alignment = 'RIGHT'
        to_vse_row.operator('preview.export_to_vse', icon='SEQUENCE')
