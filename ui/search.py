from . base_list import BASE_UL_List


class SEARCH_UL_List(BASE_UL_List):
    def draw_rating(self, layout, item, index):
        if index != 0:
            layout.label(text='Rating: {}'.format(item.rating))
