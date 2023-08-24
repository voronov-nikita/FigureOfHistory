import pygame as pg



class OpenSpace():
    def __init__(self, window_size:tuple=(500, 500), background_colour:tuple=(255, 255, 255), fps:int=30):
        self.background_colour = background_colour
        self.window_size = window_size
        self.screen = pg.display.set_mode(self.window_size)
        self.FPS = fps
        self.clock = pg.time.Clock()
        self.work = True

    def draw_ground(self):
        self.screen.fill(self.background_colour)