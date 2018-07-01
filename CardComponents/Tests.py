from CardComponents.OneLineText import OneLineText
from CardComponents.CardImage import CardImage
from CardComponents.MultilineText import MultilineText
from Card import Card

# card = Card(1920,1080,'../','testing')
# cardimage = CardImage('small_sea_wave_hdtv_1080p.jpg',1920,1080,0,0)
# oneLineText = OneLineText('testing',960,540,480,270,'ToxTypewriter.ttf')
# card.add_component(cardimage)
# card.add_component(oneLineText)
# card.print_image()

m = MultilineText('I am the very pinnacle of disaster of this world',100,100,0,0,'ToxTypewriter.ttf')
m.fit_text_to_space()


