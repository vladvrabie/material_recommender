from . base_list import BASE_UL_List


class RECOMMENDATIONS_UL_List(BASE_UL_List):
    def draw_rating(self, layout, item, index):
        layout.label(text='Rating: {}'.format(item.rating))
