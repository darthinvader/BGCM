from PIL import Image

class CardImage:

    def __init__(self, path, Sx, Sy, Lx, Ly):
        self.path = path  # The path of the photo file
        self.Sx = Sx      # The Size of X axis of the photo
        self.Sy = Sy      # The size of Y axis of the photo
        self.Lx = Lx      # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly      # The position of the photo in the Y axis (measured from up to down)
        self.card_image = (Image.open(path)).resize((Sx, Sy), Image.ANTIALIAS)

    # Add the image to the card

    def add2card(self, card):
        card.paste(self.card_image, (self.Lx, self.Ly), self.card_image)
