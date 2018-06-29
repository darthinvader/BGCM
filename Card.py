class Card:
    def __init__(self, sizex, sizey):
        self.components = []
        self.sizex = sizex
        self.sizey = sizey

    def add_component(self, component):
        self.components.append(component)
