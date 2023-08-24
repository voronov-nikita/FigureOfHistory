import pygame as pg
import sys

from Hero import Object
from Place import OpenSpace


pg.init()



# Имя нашего окна
pg.display.set_caption("NEW")

window = OpenSpace()
window.background_colour = (0, 0, 0)
screen = window.screen

number = int(input(">>> "))

list_object = [Object(window, speed=5, angle = k, size=10) for k in range(number)]

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

