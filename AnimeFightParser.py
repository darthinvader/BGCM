from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from CardComponents.OneLineText import OneLineText
from Card import Card
import csv

WIDTH = 3000;
HEIGHT = 4000;
ImagePath = "Images/"


def getCSV(filename):
    cardProperties = list()
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            cardProperties.append(row)
    print(cardProperties)
    return cardProperties


def printCard(cardProp):
    i = 0
    dragon = CardImage(ImagePath + 'dragon.png', 293, 350, 2578, 75)
    border = CardImage(ImagePath + 'CardTemplates.jpg', WIDTH, HEIGHT, 0, 0)
    tp = "   "
    for row in cardProp:

        card = Card(WIDTH, HEIGHT, '', row[0])
        image = CardImage(ImagePath + row[7], 2900, 2000, 50, 500)
        name = OneLineText(row[0].capitalize(), 2300, 400, 100, 50, "GODOFWAR.ttf", color=(255, 255, 255, 255))

        effectText = MultilineText(row[6].capitalize(), 2800, 800, 100, 2600, "GODOFWAR.ttf", color=(255, 255, 255, 255))

        type = OneLineText(row[2].capitalize(), 850, 350, 100, 3500, "GODOFWAR.ttf", color=(255, 255, 255, 255))

        ADE = OneLineText((row[3]+tp+row[4]+tp+row[5]).capitalize(), 1800, 350, 1100, 3500, "GODOFWAR.ttf", color=(255, 255, 255, 255))

        card.add_component(border)
        if row[1] == "YES":
            card.add_component(dragon)

        card.add_component(image)
        card.add_component(name)
        card.add_component(effectText)
        card.add_component(type)
        card.add_component(ADE)
        card.print_image()


cardProp = getCSV("human.csv")
printCard(cardProp)

