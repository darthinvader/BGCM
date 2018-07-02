from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from CardComponents.OneLineText import OneLineText
from Card import Card


def get_text(i, tokens):
    txt = ''
    i = i + 1
    token = tokens[i + 1]
    while token != '\'':
        txt = txt + ' ' + token
        i = i + 1
        token = tokens[i + 1]
    txt = str(txt[1:len(txt)])
    return txt, i + 1


file = open('Card_to_make.txt', 'r')

txt = file.read()
file.close()

tokens = txt.split()

directory = None
dir_flag = True
card_flag = True
one_line_flag = True
image_flag = True
multiline_flag = True
cards = list()
components = list()

length = len(tokens)

for i in range(0, length):
    t = tokens[i]
    if t == '&':
        if dir_flag:
            directory = tokens[i + 1]
            i = i + 1
            dir_flag = False
        else:
            dir_flag = True
        continue

    if t == '!' and dir_flag:
        print('Error in' + str(i) + 'Card doesnt have parent directory')
        exit(0)

    if t == '!':
        if card_flag:
            sizeX = int(tokens[i + 1])
            sizeY = int(tokens[i + 2])
            i = i + 2
            name, i = get_text(i, tokens)

            card = Card(sizeX, sizeY, directory, name)
            cards.append(card)
            card_flag = False
        else:
            for c in components:
                cards[-1].add_component(c)
                components = list()
            card_flag = True
        continue

    if t == '@' and card_flag:
        print('Error in ' + str(i) + 'Image doesnt have parent Card')
        exit(0)

    if t == '@':
        if image_flag:
            image_path, i = get_text(i, tokens)
            image = CardImage(image_path, int(tokens[i + 1]), int(tokens[i + 2]), int(tokens[i + 3]),
                              int(tokens[i + 4]))
            components.append(image)
            i = i + 4
            image_flag = False
        else:
            image_flag = True
        continue

    if t == '$' and card_flag:
        print('Error in ' + str(i) + 'OneLineText doesnt have parent Card')
        exit(0)

    if t == '$':
        if one_line_flag:
            txt, i = get_text(i, tokens)
            sizeX = int(tokens[i + 1])
            sizeY = int(tokens[i + 2])
            Lx = int(tokens[i + 3])
            Ly = int(tokens[i + 4])
            i = i + 4
            font, i = get_text(i, tokens)
            borderX = int(tokens[i + 1])
            borderY = int(tokens[i + 2])
            one_line_text = OneLineText(txt, sizeX, sizeY, Lx, Ly, font, borderX, borderY)
            components.append(one_line_text)
            one_line_flag = False
            i = i + 2
        else:
            one_line_flag = True
        continue

    if t == '%' and card_flag:
        print('Error in ' + str(i) + 'MultilineText doesnt have parent Card')
        exit(0)

    if t == '%':
        if multiline_flag:
            txt, i = get_text(i, tokens)
            sizeX = int(tokens[i + 1])
            sizeY = int(tokens[i + 2])
            Lx = int(tokens[i + 3])
            Ly = int(tokens[i + 4])
            i = i + 4
            font, i = get_text(i, tokens)
            borderX = int(tokens[i + 1])
            borderY = int(tokens[i + 2])
            one_line_text = MultilineText(txt, sizeX, sizeY, Lx, Ly, font, borderX, borderY)
            components.append(one_line_text)
            multiline_flag = False
            i = i + 2
        else:
            multiline_flag = True
        continue

for c in cards:
    c.print_image()
