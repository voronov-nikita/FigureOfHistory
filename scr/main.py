import pygame as pg
from random import randint

from component import StandartIndivid, GreenEat

pg.init()


class OpenSpace():
    def __init__(self):
        self.background_colour = (255, 255, 255)
        self.screen = pg.display.set_mode((500, 500))
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.work = True


pg.display.set_caption("Generation")


def start():

    def intersection_elems():
        for eats in list_object_eat:
            if hero.rect.colliderect(eats.rect):
                if eats.generation:
                    eats.generation = False
                else:
                    hero.point += 1
                    eats.live = False

    def update_image(pos):
        hero.update_position(pos)
        place.screen.fill(place.background_colour)
        # отрисовка
        hero.draw_hero(place.screen)
        for elem in list_object_eat:
            elem.create_food(place.screen)

        pg.display.update()

    place = OpenSpace()
    hero = StandartIndivid()

    # создаем amount_eat экземпляров еды для индивидума
    # для обозначения точного количесвта очков был взят параметр для противоположного от количества очков героя
    amount_food = 50
    list_object_eat = [GreenEat(place.screen) for _ in range(amount_food)]

    list_cord_eats = sorted([(elem.cord_x, elem.cord_y) for elem in list_object_eat])
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
        hero.move_object_hero(list_cord_eats)
        intersection_elems()

        #   <------------- Обработать все изображения -------------->
        update_image(pos)

    pg.quit()


if __name__ == "__main__":
    start()
