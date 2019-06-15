from bpy.types import UIList


class GPRUIList(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_property, index=0, flt_flag=0):
        self.use_filter_show = False
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.material_id)
            layout.prop(item, "rating", text="Rating", slider=True)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)
