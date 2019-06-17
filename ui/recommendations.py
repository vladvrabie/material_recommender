from . base_list import BaseList


class RecommendationsList(BaseList):
    def draw_rating(self, layout, item):
        layout.label(text='Rating: {}'.format(item.rating))
