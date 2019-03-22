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

card_name = OneLineText('The Great Test Image.', 390, 90,155, 10, 'DejaVuSans.ttf')
card_effect = MultilineText(
    'Gain 1 Coin and 1 Tasty.Trash 1 card from the Supermarket and draw 1 card from your Deck.', 680, 120,
    10,505, 'DejaVuSans.ttf')



card.add_component(card_name)
card.add_component(card_effect)


card.print_image()