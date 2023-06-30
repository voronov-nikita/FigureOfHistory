import pygame as pg
import sys

pg.init()


class OpenSpace():
    def __init__(self, window_size:tuple=(500, 500), background_colour:tuple=(255, 255, 255), fps:int=60):
        self.background_colour = background_colour
        self.window_size = window_size
        self.screen = pg.display.set_mode(self.window_size)
        self.FPS = fps
        self.clock = pg.time.Clock()
        self.work = True

    def draw_ground(self):
        position = (
            0, self.window_size[1]-self.window_size[1]*0.01, self.window_size[1], 5
        )
        pg.draw.rect(self.screen, (0,0,0), position)


class Square():
    def __init__(self, window_screen, size:int, color:tuple, cords:tuple=(0, 0)):
        
        self.size = size
        self.color = color

        self.screen = window_screen

        # start cords
        self.cord_x, self.cord_y = cords

        self.drawing = True



    def draw(self):
        if self.drawing:
            position = (
                self.cord_x,
                self.cord_y,
                self.size,
                self.size
            )
            pg.draw.rect(self.screen, self.color, position)


    def move(self, speed:int, moving:str):

        if moving not in ["U", "D", "R", "L"]:
            print("\nError in name of moving. Use the ['U', 'D', 'R', 'L'].\n")
            return

        size = pg.display.get_window_size()

        if moving == "U":
            if self.cord_y > size[1]:
                self.cord_y -= speed

        elif moving == "D":
            if self.cord_y + self.size * 1.19 < size[1]:
                self.cord_y += speed

        elif moving == "R":
            if self.cord_x +self.size < size[0]:
                self.cord_x += speed

        elif moving == "L":
            if self.cord_x > size[0]:
                self.cord_x -= speed


def start():
    # Имя нашего окна
    pg.display.set_caption("NEW")

    window = OpenSpace()
    screen = window.screen

    square1 = Square(screen, size=30, color=(0, 0, 0))
    square2 = Square(screen, size=30, color=(255, 0, 0))

    while window.work:
        # установка значения частоты обновления кадров
        window.clock.tick(window.FPS)

        # Обработка события выхода
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        square1.move(15, "D")
        square2.move(10, "D")


        # Обновление экрана
        screen.fill(window.background_colour)
        window.draw_ground()
        square2.draw()
        square1.draw()
        pg.display.update()
    pg.quit()


if __name__=="__main__":
    start()
