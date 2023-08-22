import pygame as pg
import random
import sys


LIST_COLORS:list[str] = ["red", "blue", "yellow", "white", "pink", "green"]

pg.init()

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



class Object():
    def __init__(self, window_screen, angle:int=1, cords:tuple=(0, 0), size:int=5):
        
        self.size = size
        self.color = random.choice(LIST_COLORS)
        self.angle = angle
        self.screen = window_screen

        # start cords
        self.cord_x, self.cord_y = cords



    def draw(self):
        pg.draw.circle(self.screen.screen, self.color, (self.cord_x, self.cord_y), self.size)
        
        
    def move_function(self, all_dot:int) -> int:
        return self.cord_x * self.angle
    
    def move(self, all_dot:int):
        self.cord_x += 1
        self.cord_y = self.move_function(all_dot)




# Имя нашего окна
pg.display.set_caption("NEW")

window = OpenSpace()
window.background_colour = (0, 0, 0)
screen = window.screen

number = int(input(">>> "))

list_object = [Object(window, angle = k, cords=(window.window_size[0]//2, window.window_size[1]//2), size=10) for k in range(number)]

while window.work:
    # установка значения частоты обновления кадров
    window.clock.tick(window.FPS)

    # Обработка события выхода
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
            
    # отрисовка
    window.draw_ground()
    for elems in list_object:
        elems.move(3)
        elems.draw()
        
    pg.display.update()

pg.quit()

