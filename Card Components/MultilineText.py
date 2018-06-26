
class MultilineText:

    def __init__(self, text, Sx, Sy, Lx, Ly, font):
        self.text = text
        self.Sx = Sx  # The Size of X axis of the photo
        self.Sy = Sy  # The size of Y axis of the photo
        self.Lx = Lx  # The position of the photo in the X axis (measured from right to left )
        self.Ly = Ly  # The position of the photo in the Y axis (measured from up to down)
        self.font = font

