from PIL import ImageFont,Image,ImageDraw
import math
from numpy import Inf


class MultilineText:

    def __init__(self, text, Sx, Sy, Lx, Ly, font):
        self.text = text
        self.Sx = Sx  # The Size of X axis of the photo
        self.Sy = Sy  # The size of Y axis of the photo
        self.Lx = Lx  # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly  # The position of the photo in the Y axis (measured from up to down)
        self.font = font

    def fit_text_to_space(self):
        font_size = 100
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(self.text, font_load)
        txt_width = txt_size[0] / font_size
        txt_height = txt_size[1] / font_size

        font_size = math.floor(math.sqrt((self.Sx * self.Sy) / (txt_width * txt_height)))
        word_size = self.word_size_calc(font_size)
        max_word_size = 0
        for ws in word_size:
            if ws > max_word_size:
                max_word_size = ws

        if max_word_size > self.Sx:
            font_size = math.floor(font_size*(self.Sx/max_word_size))

        txt_size, max_lines = self.text_width_calc(font_size)

        result = self.solve_wrap(word_size, max_lines)

        flag = True
        wsl = len(word_size)
        while flag:
            if not test_max_line_viability(max_lines, result):
                font_size = font_size-1
                txt_size, max_lines = self.text_width_calc(font_size)
                word_size = self.word_size_calc(font_size)
                result = self.solve_wrap(word_size, max_lines)
                continue
            else:
                flag = False
        return font_size

    def solve_wrap(self, word_size, max_lines):
        wsl = len(word_size)

        cost = [[0 for x in range(wsl)] for y in range(wsl)]
        cost_squared = [[0 for x in range(wsl)] for y in range(wsl)]

        min_cost = [0 for x in range(wsl)]
        result = [0 for x in range(wsl)]

        for i in range(0, wsl):
            cost[i][i] = self.Sx - word_size[i]
            cost_squared[i][i] = cost[i][i]**2
            for j in range(i+1, wsl):
                cost[i][j] = cost[i][j-1] - word_size[j] - 1
                if cost[i][j] < 0:
                    cost_squared[i][j] = Inf
                else:
                    cost_squared[i][j] = cost[i][j]**2

        for i in range(wsl-1, -1, -1):
            min_cost[i] = cost_squared[i][wsl-1]
            result[i] = wsl
            for j in range(wsl-1, i, -1):
                if cost_squared[i][j-1] == Inf:
                    continue
                if min_cost[i] > min_cost[j] + cost_squared[i][j-1]:
                    min_cost[i] = min_cost[j] + cost_squared[i][j-1]
                    result[i] = j



        return result

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

    def text_width_calc(self, font_size):
        font_load = ImageFont.truetype(self.font, font_size)
        txt_image = Image.new('RGBA', (self.Sx, self.Sy), (255, 255, 255, 0))
        d = ImageDraw.Draw(txt_image)
        txt_size = d.textsize(self.text, font_load)
        max_lines = math.floor(self.Sy / txt_size[1])
        return txt_size, max_lines


def test_max_line_viability(max_lines, result):
    flag = True
    i = 1
    count = 0
    print(result)
    length = len(result)
    while flag:
        if i >= length:
            flag = False
            break
        count = count + 1
        i = result[i]

    return max_lines >= count
