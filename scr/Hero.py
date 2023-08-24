import pygame as pg
import random


LIST_COLORS:list[str] = ["red", "blue", "yellow", "white", "pink", "green"]


class Object():
    def __init__(self, window_screen, angle:int=1, size:int=5, speed:int=1):
        
        self.size = size
        self.color = random.choice(LIST_COLORS)
        self.angle = angle
        self.screen = window_screen
        self.speed:int = speed
        self.isRight:bool = True

        # start cords
        self.cord_x, self.cord_y = 250 ,250


    def draw(self):
        pg.draw.circle(self.screen.screen, self.color, (self.cord_x, self.cord_y), self.size)
        
        
    def move_function(self, all_dot:int) -> int:
        if self.angle % 2 == 0:
            return self.screen.window_size[1] // 2 + self.cord_x * self.angle
        return self.screen.window_size[1] // 2 - self.cord_x * (self.angle - 1)
    
    
    def move(self, all_dot:int):
        if self.isRight:
            if self.cord_x >= self.screen.window_size[0] * 0.5:
                self.isRight = False
            self.cord_x += self.speed
            self.cord_y = self.move_function(all_dot)
        else:
            if self.cord_x <= self.screen.window_size[0] * 0.1:
                self.isRight = True
            self.cord_x -= self.speed
            self.cord_y = self.move_function(all_dot)