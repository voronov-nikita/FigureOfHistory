import pygame as pg
import math



class Hero():
    def __init__(self, start_cords:tuple, size:int, speed:int, color:tuple=(0, 0, 0)):
        self.cord_x, self.cord_y = start_cords
        self.size:int = size
        self.color:tuple = color
        self.speed:int = speed
        
        # testing
        self.cord_y = 250
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.cord_x, self.cord_y), self.size)
    
    
    def function_y(self):
        return (math.cos(self.cord_x) * 10)


    def move(self, count_point:int, special_speed:int=-1):
        speed = (special_speed, self.speed)[special_speed==-1]
        angle:int = 360 // count_point
        k = math.sin(angle) // math.cos(angle)
        
        self.cord_x += speed
        self.cord_y = k * self.cord_x


class Window():
    def __init__(self, win_name:str, win_size:tuple=(500, 500), background_color:tuple=(255, 255, 255)):
        self.window_size:tuple = win_size
        self.window_name:str = win_name
        
        self.bg_color:tuple = background_color
        
        self.screen = None
        self.clock = pg.time.Clock()
        self.FPS:int = 30
        
        self.run:bool = True
        # generate main UI
        self.initUI()
        
    def initUI(self):
        self.screen = pg.display.set_mode(self.window_size)
        # SET Name for window
        pg.display.set_caption(self.window_name)
        
        
    def draw_ground(self):
        self.screen.fill(self.bg_color)
        
        