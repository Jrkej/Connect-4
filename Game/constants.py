import os

class const():
    def __init__(self):
        self.directory = os.path.dirname(__file__)
        self.resource_dir = self.directory + "\\resources"

        self.WIDTH = 7
        self.HEIGHT = 6
        self.FONT_SIZE = 25
        self.TIMES = 4
        
        self.WIDTH_DISPLAY = (self.WIDTH * 100) + 200
        self.HEIGHT_DISPLAY = (self.HEIGHT * 100) + 50

        self.BG = (2, 255, 0)