from pico2d import *

open_canvas()

warrior = load_image('WarriorSprite.png')

for frame in range(4):
    clear_canvas()
    warrior.clip_draw(225 + frame * 165, 839, 140, 140,
                      400, 300, 280, 280)
    update_canvas()
    delay(0.2)

delay(3)
close_canvas()