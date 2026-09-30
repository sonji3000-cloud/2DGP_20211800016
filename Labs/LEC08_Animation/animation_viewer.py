from pico2d import *

open_canvas()

warrior = load_image('WarriorSprite.png')

while(True):
    for frame in range(4):
        clear_canvas()
        warrior.clip_draw(225 + frame * 165, 839, 140, 140,
                          400, 300, 280, 280)
        update_canvas()
        delay(0.2)

    for frame in range(8):
        clear_canvas()
        warrior.clip_draw(195 + frame * 165, 649, 140, 150,
                          400, 300, 280, 300)
        update_canvas()
        delay(0.2)

close_canvas()
