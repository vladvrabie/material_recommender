from bpy.types import UIList


class BaseList(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_property, index=0, flt_flag=0):
        self.use_filter_show = False
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.id)
            self.draw_rating(layout, item)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)
