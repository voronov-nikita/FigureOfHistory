import pygame as pg
from random import randint

from component import Standartindivid, GreenEat

pg.init()


class OpenSpace():
    def __init__(self):
        self.background_colour = (255, 255, 255)
        self.screen = pg.display.set_mode((500, 500))
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.work = True

    def restart_screen(self):
        pass


class Individ(Standartindivid):
    def __init__(self, window):
        self.size_individ = 10

        self.cord_x = randint(0, 500)
        self.cord_y = randint(0, 500)

        self.life = True
        
        self.surface = pg.Surface((self.size_individ, self.size_individ))
        self.rect = self.surface.get_rect()

        self.color = (255, 0, 0)
        self.position = (self.cord_x,
                         self.cord_y,
                         self.size_individ,
                         self.size_individ)

    def draw_hero(self, screen):
        pg.draw.rect(screen, self.color, self.position)
        self.surface.fill(self.color)
        self.rect.x = self.cord_x
        self.rect.y = self.cord_y
        screen.blit(self.surface, self.rect)

    def update_position(self, new_pos: tuple):
        self.position = new_pos


def move_object_hero():
    keys_button = pg.key.get_pressed()

    if keys_button[pg.K_LEFT] and hero.move_left(hero.cord_x):
        hero.cord_x -= 10
    if keys_button[pg.K_RIGHT] and hero.move_right(hero.cord_x, hero.size_individ):
        hero.cord_x += 10
    if keys_button[pg.K_UP] and hero.move_up(hero.cord_y):
        hero.cord_y -= 10
    if keys_button[pg.K_DOWN] and hero.move_down(hero.cord_y, hero.size_individ):
        hero.cord_y += 10


def intersection_elems():
    for eats in list_object_eat:
        if hero.rect.colliderect(eats.rect):
            eats.live = True

pg.display.set_caption("Generation")
place = OpenSpace()
hero = Individ(place.screen)

# создаем amount_eat экземпляров еды для индивидума
amount_food = 50
list_object_eat = []
for i in range(amount_food):
    eat = GreenEat(place.screen)
    list_object_eat.append(eat)

while place.work:
    place.clock.tick(place.FPS)

    # проверка на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            place.work = False
    # движение
    move_object_hero()
    intersection_elems()

    pos = (hero.cord_x,
           hero.cord_y,
           hero.size_individ,
           hero.size_individ)

    #   <------------- Обработать все изображения -------------->
    hero.update_position(pos)
    place.screen.fill(place.background_colour)
    # отрисовка
    hero.draw_hero(place.screen)
    for elem in list_object_eat:
        elem.create_food(place.screen)
    

    pg.display.update()

pg.quit()
