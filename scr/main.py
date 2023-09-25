import pygame as pg
import random
from hero import Window, Hero, Enemy


pg.init()

def check_click_button() -> str:
    keys_button = pg.key.get_pressed()
    if keys_button[pg.K_LEFT]:
        return "left"
    elif keys_button[pg.K_RIGHT]:
        return "right"
    elif keys_button[pg.K_DOWN]:
        return "down"
    elif keys_button[pg.K_UP]:
        return "up"
    return None


# <----------------------- MAIN GAME ------------------------>

window = Window("NEW", background_color=(0, 0, 0))
hero = Hero(20, 5, (255, 255, 0))
enemy:list = []
for _ in range(random.randint(0, 10)):
    enemy.append(Enemy(window, hero, size=20))
direction_hero = None
while window.run:
    window.clock.tick(window.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window.run = False
    
    
    direction_hero = (check_click_button(), direction_hero)[check_click_button() is None]
    if direction_hero is not None and hero.ability_go(window):
        hero.move(direction_hero)
        
        
    # drawing
    window.draw_ground()
    hero.draw(window.screen)
    for elem in enemy:
        elem.draw(window.screen)
    pg.display.update()

pg.quit()
exit(0)
