import pygame as pg

from hero import Window, Hero


pg.init()


window = Window("NEW")
hero = Hero((0, 0), 10, 2)

while window.run:
    window.clock.tick(window.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window.run = False
    
    hero.move('right')
    
    # drawing
    window.draw_ground()
    hero.draw(window.screen)
    pg.display.update()

pg.quit()
exit(0)
