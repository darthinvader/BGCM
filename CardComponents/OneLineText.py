from PIL import ImageDraw, Image, ImageFont

import math


class OneLineText:

    def __init__(self, text, Sx, Sy, Lx, Ly, font):
        self.text = text
        self.Sx = Sx  # The Size of X axis of the photo
        self.Sy = Sy  # The size of Y axis of the photo
        self.Lx = Lx  # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly  # The position of the photo in the Y axis (measured from up to down)
        self.font = font

    def add_to_card(self, card):
        font_size, txt_size = self.find_font_size()
        pos = self.get_starting_pos(txt_size)
        d = ImageDraw.Draw(card)
        font_load = ImageFont.truetype(self.font, font_size)
        d.text(pos, self.text, font=font_load, fill=(255, 255, 255, 0))

    def find_font_size(self):
        font_load = ImageFont.truetype(self.font, 100)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(self.text, font_load)
        txt_width = txt_size[0] / 100
        txt_height = txt_size[1] / 100
        font_width = math.floor(self.Sx / txt_width)
        font_height = math.floor(self.Sy / txt_height)

        if font_width > font_height:
            font_size = font_height
        else:
            font_size = font_width

        font_load = ImageFont.truetype(self.font, font_size)
        txt_size = d.textsize(self.text, font_load)

        return font_size, txt_size

    def get_starting_pos(self, txt_size):
        print(txt_size)
        posx = self.Lx + (self.Sx)/2 - txt_size[0]/2
        posy = self.Ly + (self.Sy)/2 - txt_size[1]/2

        return posx, posy