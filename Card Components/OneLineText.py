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


    def find_font_size(self):
        FontLoad = ImageFont.truetype(self.font, 100)
        txtImage = Image.new('RGBA', (1000,1000), (255, 255, 255, 0))
        d = ImageDraw.Draw(txtImage)
        txtsize = d.textsize(self.text, FontLoad)
        txtWidth = txtsize[0] / 100
        txtHeight = txtsize[1] / 100
        fontWidth = math.floor(self.Sx / txtWidth)
        fontHeight = math.floor(self.Sy / txtHeight)


        if fontWidth > fontHeight:
            fontSize = fontHeight
        else:
            fontSize = fontWidth

        FontLoad = ImageFont.truetype(self.font, fontSize)
        txtsize = d.textsize(self.text, FontLoad)

        return fontSize, txtsize