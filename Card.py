from PIL import Image


class Card:
    def __init__(self, sizex, sizey, save_path, image_name):
        self.components = []
        self.sizex = sizex
        self.sizey = sizey
        self.card = Image.new('RBGA', (self.sizex, self.sizey), 'White')
        self.save_path = save_path
        self.image_name = image_name

    def add_component(self, component):
        self.components.append(component)

    def print_image(self):
        for c in self.components:
            c.add_to_card(self)
        self.card.save(self.save_path + self.image_name + '.png', 'PNG')
