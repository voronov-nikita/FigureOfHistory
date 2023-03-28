from random import randint
import pygame as pg


def new_random_coords(edges):
    return randint(edges, 500 - edges)


class StandartIndivid(pg.Rect):

    def __init__(self):
        super().__init__(self)
        self.size_individ = 10
        self.speed = 5
        self.point = 0

        self.cord_x = randint(0, 500)
        self.cord_y = randint(0, 500)
        self.count_point = 0

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
    
    def move_object_hero(self, list_cord: list):
        try:
            elem = list_cord[self.count_point]

            if self.cord_x >= elem[0] and self.move_left(self.cord_x):
                self.cord_x -= self.speed
            elif self.cord_x <= elem[0] and self.move_right(self.cord_x, self.size_individ):
                self.cord_x += self.speed

            if self.cord_y >= elem[1] and self.move_up(self.cord_y):
                self.cord_y -= self.speed
            elif self.cord_y <= elem[1] and self.move_down(self.cord_y, self.size_individ):
                self.cord_y += self.speed

            if elem[0] in range(self.cord_x-self.size_individ, self.cord_x+self.size_individ//2) and elem[1] in range(self.cord_y-self.size_individ//2, self.cord_y+self.size_individ//2):
                self.count_point += 1

                print(self.point)

        except IndexError:
            pass


class GreenEat(pg.Rect):
    def __init__(self, window):
        super().__init__(self)
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
