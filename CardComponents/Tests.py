from CardComponents.OneLineText import OneLineText
from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from Card import Card

card = Card(700, 1000, '../', 'testing')
type_border = CardImage('Images/Type border.jpg', 150, 150, 0, 0)
coin_border = CardImage('Images/Coin border.jpg', 150, 150, 550, 0)
name_border = CardImage('Images/Name border.jpg', 400, 100, 150, 0)
text_border = CardImage('Images/Text border.jpg', 700, 500, 0, 500)
card_border = CardImage('Images/Card Border.png', 700, 1000, 0, 0)

card.add_component(type_border)
card.add_component(coin_border)
card.add_component(name_border)
card.add_component(text_border)
card.add_component(card_border)

card_name = OneLineText('The Great Test Image.', 1300, 200, 100, 125, 'DejaVuSans.ttf')
card_effect = MultilineText(
    'The Great effect that has some text her and its going to be grant and stuff i dont know maybe.Something about some abilities and stuff.',
    1300, 650, 100, 1225, 'DejaVuSans.ttf', 100, 200)

card.add_component(card_name)
card.add_component(card_effect)
card.print_image()