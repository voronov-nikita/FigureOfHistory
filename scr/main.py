import pygame as pg
from random import randint

from component import Standartindivid


class OpenSpace():
    def __init__(self):
        self.background_colour = (255, 255, 255)
        self.screen = pg.display.set_mode((500, 500))
        pg.display.set_caption("Generation")
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.work = True


class Individ(Standartindivid):
    def __init__(self):
        self.size_individ = 10

        self.cord_x = randint(0, 500)
        self.cord_y = randint(0, 500)

        self.life = True

        self.color = (255, 0, 0)
        self.position = (self.cord_x, 
                         self.cord_y, 
                         self.size_individ, 
                         self.size_individ)

    def draw_hero(self, screen):
        pg.draw.rect(screen, self.color, self.position)

    def update_position(self, new_pos:tuple):
        self.position = new_pos



place = OpenSpace()
hero = Individ()

while place.work:
    place.clock.tick(place.FPS)
     
    # проверка на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            place.work = False

    # список нажатых клавиш
    keys_button = pg.key.get_pressed()

    if keys_button[pg.K_LEFT] and hero.move_left(hero.cord_x):
        hero.cord_x -= 10
    if keys_button[pg.K_RIGHT] and hero.move_right(hero.cord_x, hero.size_individ):
        hero.cord_x += 10
    if keys_button[pg.K_UP] and hero.move_up(hero.cord_y):
        hero.cord_y -= 10
    if keys_button[pg.K_DOWN] and hero.move_down(hero.cord_y, hero.size_individ):
        hero.cord_y += 10

    pos = ( hero.cord_x,
            hero.cord_y,
            hero.size_individ,
            hero.size_individ)

    hero.update_position(pos)
    place.screen.fill(place.background_colour)
    # отрисовка героя
    hero.draw_hero(place.screen)
    
    pg.display.update()

pg.quit()

