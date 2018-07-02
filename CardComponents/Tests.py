from CardComponents.OneLineText import OneLineText
from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from Card import Card

card = Card(1500, 2000, '../', 'testing')
yellow_image = CardImage('../yellow area.jpg', 1300, 200, 100, 125)
green_image = CardImage('../green area.jpg', 1300, 700, 100, 425)
blue_image = CardImage('../blue_area.jpg', 1300, 650, 100, 1225)
card.add_component(yellow_image)
card.add_component(green_image)
card.add_component(blue_image)

card_name = OneLineText('The Great Test Image.', 1300, 200, 100, 125, 'CRACJ___.ttf')
card_effect = MultilineText(
    'The Great effect that has some text her and its going to be grant and stuff i dont know maybe.Something about some abilities and stuff.',
    1300, 650, 100, 1225, 'CRACJ___.ttf', 100, 200)

card.add_component(card_name)
card.add_component(card_effect)

card.print_image()