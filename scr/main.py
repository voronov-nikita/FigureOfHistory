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
        self.work = False
        start()


class Individ(Standartindivid):
    def __init__(self, window):
        super().__init__(self)
        self.size_individ = 10
        self.speed = 10

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


pg.display.set_caption("Generation")


def start():
    def move_object_hero(list_cord: list, pos: tuple):

        for elem in list_cord:
            while hero.cord_x-hero.size_individ//2 > elem[0]:
                hero.cord_x -= hero.speed
                update_image(pos)
            while hero.cord_x-hero.size_individ//2 < elem[0]:
                hero.cord_x += hero.speed
                update_image(pos)
            while hero.cord_y-hero.size_individ//2 > elem[1]:
                hero.cord_y += hero.speed
                update_image(pos)
            while hero.cord_y-hero.size_individ//2 < elem[1]:
                hero.cord_y -= hero.speed
                update_image(pos)

    def intersection_elems():
        for eats in list_object_eat:
            if hero.rect.colliderect(eats.rect):
                if eats.generation:
                    print("OK\n")
                    eats.generation = False
                else:
                    eats.live = False

    def update_image(pos):
        hero.update_position(pos)
        place.screen.fill(place.background_colour)
        # отрисовка
        hero.draw_hero(place.screen)
        for elem in list_object_eat:
            elem.create_food(place.screen)

        pg.display.update()

    def sort_list(ls: list):
        print(sorted(ls))

    place = OpenSpace()
    hero = Individ(place.screen)

    # создаем amount_eat экземпляров еды для индивидума
    amount_food = 50
    list_object_eat = [GreenEat(place.screen) for _ in range(amount_food)]

    list_cord_eats = [(elem.cord_x, elem.cord_y) for elem in list_object_eat]
    sort_list(list_cord_eats)
    while place.work:
        place.clock.tick(place.FPS)

        # проверка на закрытие экрана
        for event in pg.event.get():
            if event.type == pg.QUIT:
                place.work = False
        # движение

        pos = (hero.cord_x,
               hero.cord_y,
               hero.size_individ,
               hero.size_individ)
        move_object_hero(list_cord_eats, pos)
        intersection_elems()

        #   <------------- Обработать все изображения -------------->
        update_image(pos)

    pg.quit()


if __name__ == "__main__":
    start()
