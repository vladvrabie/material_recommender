from . base_list import BaseList


class PreferencesList(BaseList):
    def draw_rating(self, layout, item):
        layout.prop(item, "rating", text="Rating", slider=True)
