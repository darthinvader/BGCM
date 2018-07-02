from CardComponents.OneLineText import OneLineText
from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from Card import Card

card = Card(1920, 1080, '../', 'testing')
cardimage = CardImage('airplane_4269.jpg', 1920, 1080, 0, 0)
oneLineText = OneLineText('testing',960,540,480,270,'ToxTypewriter.ttf')
card.add_component(cardimage)
card.add_component(oneLineText)

m = MultilineText('Lorem ipsum dolor sit amet.',300, 100, 1500, 900, 'ToxTypewriter.ttf')
card.add_component(m)
card.print_image()
# m.fit_text_to_space()
