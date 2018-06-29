from CardComponents.OneLineText import OneLineText
from Card import Card

card = Card(1920,1080,'../','testing')
oneLineText = OneLineText('testing',1820,980,100,100,'ToxTypewriter.ttf')
card.add_component(oneLineText)
card.print_image()
