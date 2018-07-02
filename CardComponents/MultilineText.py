from PIL import ImageFont, Image, ImageDraw
import math
from numpy import Inf


class MultilineText:

    def __init__(self, text, Sx, Sy, Lx, Ly, font, borderX = 0, borderY = 0):
        self.text = text
        self.font = font
        self.Sx = Sx-borderX  # The Size of X axis of the photo
        self.Sy = Sy-borderY  # The size of Y axis of the photo
        self.Lx = Lx+(borderX/2)  # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly+(borderY/2)  # The position of the photo in the Y axis (measured from up to down)

    def add_to_card(self, card):
        # Calculate font size and the lines its going to draw
        font_size, lines = self.fit_text_to_space()

        # Load the font and the Image of the card
        font_load = ImageFont.truetype(self.font, font_size)
        d = ImageDraw.Draw(card)

        # Get the position of each line
        line_pos = self.calc_line_pos(lines, font_size)

        # Draw each line at their correct position
        i = 0
        for lp in line_pos:
            line = lines[i]
            outline_maker(d, lp, line, font_load, (255, 255, 255, 255))
            d.text(lp, line, font=font_load, fill=(0,0,0, 255))
            i = i + 1

    # This function returns the font and the lines of the Text
    def fit_text_to_space(self):
        # Basic variables to use later for the calculations
        font_size = 100
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)

        # This calculates the width and height of the text in a single line of size 1 of the current font
        # (It is not really size 1 because if it was it would lose precision so i use font 100 and then divide by 100
        # which is more precise)
        txt_size = d.textsize(self.text, font_load)
        txt_width = txt_size[0] / font_size
        txt_height = txt_size[1] / font_size

        # The calculation below is being thought like this
        # We have a rectangular space that we want to fit our lines
        # So in order to determine a good approximation of the font size we take the width and height of the text
        # and calculate that as a rectangular area T = (x*y)
        # then we take the size of our rectangle we want to fit our text S for the area of the rectangle
        # Divide that by T => S/T
        # That gives as how much bigger the rectangle is than our text rectangle
        # And lastly we take its square root because the font_size increases both height and width proportionally
        # so by square rooting we get our approximation for the font_size
        # This approximation will be almost always bigger or equal to our actual font_size we need
        # Example below
        # Our space to fill:
        # |-----------|
        # |           |
        # |           |
        # |           |
        # |           |
        # |-----------|
        # 11*6
        # Our Text Line :
        # |-----|
        # |-----|
        # 5 * 2
        # So the second square is (11*6)/(5*2) = 6.6 smaller than the first
        # So we need to multiply the Text line's each side by root(6.6) = 2.5
        # To get a square with the same area
        # The flooring in the line below is done because font can't be a float number

        font_size = math.floor(math.sqrt((self.Sx * self.Sy) / (txt_width * txt_height)))

        # We take the biggest word width so we know it can fit in a single line alone
        word_size = self.word_size_calc(font_size)
        max_word_size = 0
        for ws in word_size:
            if ws > max_word_size:
                max_word_size = ws

        # If it cannot the we reduce our font_size to a size that it will make our word fit
        if max_word_size > self.Sx:
            font_size = math.floor(font_size * (self.Sx / max_word_size))

        # Then we start to calculate the separation of the words in lines
        txt_size, max_lines = self.text_width_calc(font_size)
        space_width = self.line_size_calc(' ', font_size)[0]
        result = self.solve_wrap(word_size, space_width)

        flag = True

        # And if the words don't fit in the maximum amount of lines we have
        while flag:
            # We reduce the size of the font by 1 until they do
            if not test_max_line_viability(max_lines, result):
                font_size = font_size - 1
                txt_size, max_lines = self.text_width_calc(font_size)
                word_size = self.word_size_calc(font_size)
                space_width = self.line_size_calc(' ', font_size)[0]
                result = self.solve_wrap(word_size, space_width)
                continue
            else:
                flag = False

        # Then we take those words in tuples (for example line 1 will be from word 1 to word 5 ,
        # line 2 from 6 to 8 and so on)
        word_tuples = word_break(result)
        words = self.text.split()
        lines = lines_calc(words, word_tuples)
        # We return the font_size and the lines of text
        return font_size, lines

    # This is a dynamic programming algorithm to solve word wrapping problem

    def solve_wrap(self, word_size, space_width):
        wsl = len(word_size)

        cost = [[0 for x in range(wsl)] for y in range(wsl)]
        cost_squared = [[0 for x in range(wsl)] for y in range(wsl)]

        min_cost = [0 for x in range(wsl)]
        result = [0 for x in range(wsl)]

        for i in range(0, wsl):
            cost[i][i] = self.Sx - word_size[i]
            cost_squared[i][i] = cost[i][i] ** 2
            for j in range(i + 1, wsl):
                cost[i][j] = cost[i][j - 1] - word_size[j] - space_width
                if cost[i][j] < 0:
                    cost_squared[i][j] = Inf
                else:
                    cost_squared[i][j] = cost[i][j] ** 2

        for i in range(wsl - 1, -1, -1):
            min_cost[i] = cost_squared[i][wsl - 1]
            result[i] = wsl
            for j in range(wsl - 1, i, -1):
                if cost_squared[i][j - 1] == Inf:
                    continue
                if min_cost[i] > min_cost[j] + cost_squared[i][j - 1]:
                    min_cost[i] = min_cost[j] + cost_squared[i][j - 1]
                    result[i] = j
        return result

    # This function is a helper function to calculate each word's size

    def word_size_calc(self, font_size):
        words = self.text.split()
        word_size = list()
        for w in words:
            font_load = ImageFont.truetype(self.font, font_size)
            txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
            d = ImageDraw.Draw(txt_image)
            txt_size = d.textsize(w, font_load)
            word_size.append(txt_size[0])
        return word_size

    # This function is a helper function to calculate the total width of the text
    def text_width_calc(self, font_size):
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(self.text, font_load)
        max_lines = math.floor(self.Sy / txt_size[1])
        return txt_size, max_lines

    # This function is a helper function to calculate the position of each line's position
    def calc_line_pos(self, lines, font_size):
        height = 0
        poses = list()
        for l in lines:
            poses.append((self.Lx, self.Ly + height))
            txt_size = self.line_size_calc(l, font_size)
            height = height + txt_size[1]

        return poses

    # This calculates the specified line size
    def line_size_calc(self, line, font_size):
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(line, font_load)
        return txt_size


# This is a helper function to check if the line sequence can be filled to the space we have
def test_max_line_viability(max_lines, result):
    i = 0
    count = 0
    length = len(result)
    while 1 == 1:
        if i >= length:
            break
        count = count + 1
        i = result[i]

    return max_lines >= count


# This is a helper function to calculate the tuple of continuous words indexes in lines
def word_break(result):
    i = 0
    flag = True
    length = len(result)
    word_tuple = list()
    while flag:
        if i >= length:
            break
        word_tuple.append((i, result[i]))
        i = result[i]

    return word_tuple


# This helper function returns the text lines for the text in working order
def lines_calc(words, word_tuple):
    lines = list()
    for w in word_tuple:
        word = words[w[0]]
        for i in range(w[0] + 1, w[1]):
            word = word + ' ' + words[i]
        lines.append(word)
    return lines


# This is a helper function that makes a text outline
def outline_maker(d, pos, text, font_load, fill):
    d.text((pos[0] + 1, pos[1] + 1), text, font=font_load, fill=fill)
    d.text((pos[0] + 1, pos[1]), text, font=font_load, fill=fill)
    d.text((pos[0] + 1, pos[1] - 1), text, font=font_load, fill=fill)
    d.text((pos[0] - 1, pos[1]), text, font=font_load, fill=fill)
    d.text((pos[0] - 1, pos[1] + 1), text, font=font_load, fill=fill)
    d.text((pos[0] + 1, pos[1]), text, font=font_load, fill=fill)
    d.text((pos[0], pos[1] + 1), text, font=font_load, fill=fill)
    d.text((pos[0], pos[1] - 1), text, font=font_load, fill=fill)
