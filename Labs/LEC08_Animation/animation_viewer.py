from pico2d import *

open_canvas()

warrior = load_image('WarriorSprite.png')

clear_canvas()
warrior.clip_draw(225, 839, 140, 140, 400, 300, 280, 280)
update_canvas()
delay(5)

close_canvas()
