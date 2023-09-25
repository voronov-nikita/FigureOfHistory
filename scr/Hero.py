import pygame as pg
import random



class Hero():
    def __init__(self,size:int, speed:int, color:tuple=(0, 0, 0)):
        self.size:int = size
        self.color:tuple = color
        self.speed:int = speed
        
        # testing
        self.cord_x = 250
        self.cord_y = 1
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.cord_x, self.cord_y, self.size, self.size))
        
    def ability_go(self, screen) -> bool:
        flag = [False, False, False, False]
        if self.cord_x < screen.window_size[0] - self.size:
            flag[0] = True
        if self.cord_x > 0:
            flag[1] = True
        if self.cord_y < screen.window_size[1] - self.size:
            flag[2] = True
        if self.cord_y > 0:
            flag[3] = True
            
        return all(flag)
        
    def move(self, direction:str):
        direct = direction.lower()
        if direct== "right":
            self.cord_x += self.speed
        elif direct == "left":
            self.cord_x -= self.speed
        elif direct == "up":
            self.cord_y -= self.speed
        elif direct == "down":
            self.cord_y += self.speed
        else:
            return ValueError()



class Enemy():
    def __init__(self, screen, hero, size:int=10, speed:int=7, color:tuple=(255, 0, 0)):
        self.screen = screen
        self.hero = hero
        
        self.color= color
        self.speed = speed
        self.size = size
        self.cord_x = random.randint(0, screen.window_size[0])
        self.cord_y = random.randint(0, screen.window_size[1])
        
        

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.cord_x, self.cord_y, self.size, self.size))
    


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
        
        