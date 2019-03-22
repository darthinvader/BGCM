from PIL import ImageDraw, Image, ImageFont
from CardComponents import MultilineText as Mt
import math


class OneLineText:

    def __init__(self, text, Sx, Sy, Lx, Ly, font, borderX = 0, borderY = 0,outline=False, center=True, color=(0,0,0,255), outlineC=(0,0,0,255)):
        self.text = text
        self.font = font
        self.Sx = Sx - borderX  # The Size of X axis of the photo
        self.Sy = Sy - borderY  # The size of Y axis of the photo
        self.Lx = Lx + (borderX / 2)  # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly + (borderY / 2)  # The position of the photo in the Y axis (measured from up to down)
        self.outline = outline
        self.center = center
        self.color = color
        self.outlineC = outlineC

    def add_to_card(self, card):
        font_size, txt_size = self.find_font_size()
        pos = self.get_starting_pos(txt_size)
        d = ImageDraw.Draw(card)
        font_load = ImageFont.truetype(self.font, font_size)
        if self.outline:
            Mt.outline_maker(d, pos, self.text, font_load, self.outlineC)
        d.text(pos, self.text, font=font_load, fill=self.color)

    def find_font_size(self):
        font_size = 100
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(self.text, font_load)
        txt_width = txt_size[0] / font_size
        txt_height = txt_size[1] / font_size
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
        posx = self.Lx
        posy = self.Ly
        if self.center:
            posx = self.Lx + self.Sx/2 - txt_size[0]/2
            posy = self.Ly + self.Sy/2 - txt_size[1]/2

        return posx, posy
