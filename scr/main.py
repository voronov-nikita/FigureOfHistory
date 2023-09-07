import pygame as pg

from hero import Window, Hero


pg.init()


window = Window("NEW")
list_hero = [Hero((0, 0), 10, 2) for _ in range(2)]

while window.run:
    window.clock.tick(window.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window.run = False
    
    for ind, hero in enumerate(list_hero):
        hero.move(ind + 1)
    
    # drawing
    window.draw_ground()
    for hero in list_hero:
        hero.draw(window.screen)
    pg.display.update()

pg.quit()
exit(0)
