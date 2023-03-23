from random import randint
import pygame as pg


def new_random_coords(edges):
    return randint(edges, 500 - edges)


class Standartindivid(pg.Rect):

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


class GreenEat(pg.Rect):
    def __init__(self, window):
        self.color = (0, 255, 0)
        self.size_object = 10

        self.generation = True
        self.live = True

        self.cord_x = new_random_coords(self.size_object)
        self.cord_y = new_random_coords(self.size_object)
        
        self.surface = pg.Surface((self.size_object, self.size_object))
        self.rect = self.surface.get_rect()

    def create_food(self, screen):
        if self.live:
            position = (self.cord_x,
                        self.cord_y,
                        self.size_object,
                        self.size_object)
            pg.draw.rect(screen, self.color, position)
            self.surface.fill(self.color)
            self.rect.x = self.cord_x
            self.rect.y = self.cord_y
            screen.blit(self.surface, self.rect)
