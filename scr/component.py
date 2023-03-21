from random import randint
import pygame as pg


def new_random_coords(edges):
    return randint(edges, 500 - edges)


class Standartindivid():

    def move_right(self, cord_x, size_individ):
        if cord_x < 500 - size_individ - 5:
            return True
        return False

    def move_left(self, cord_x):
        if cord_x > 0:
            return True
        return False

    def move_up(self, cord_y):
        if cord_y > 1:
            return True
        return False

    def move_down(self, cord_y, size_individ):
        if cord_y < 500 - size_individ - 5:
            return True
        return False


class GreenEat():
    def __init__(self, window):
        self.color = (0, 255, 0)
        self.size_object = 10

        self.rect = pg.Rect(*window.get_rect().center, 100, 100)
        self.cord_x = new_random_coords(self.size_object)
        self.cord_y = new_random_coords(self.size_object)

    def create_food(self, screen):
        position = (self.cord_x,
                    self.cord_y,
                    self.size_object,
                    self.size_object)
        pg.draw.rect(screen, self.color, position)
