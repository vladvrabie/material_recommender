from . base_list import BASE_UL_List


class PREFERENCES_UL_List(BASE_UL_List):
    def draw_rating(self, layout, item, index):
        layout.prop(item, "rating", text="Rating", slider=True)
