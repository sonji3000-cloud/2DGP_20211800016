from pico2d import *

open_canvas()

warrior = load_image('WarriorSprite.png')


def draw_frame(left, bottom, width, height):
    warrior.clip_draw(
        left, bottom, width, height,
        400, 300, width * 2, height * 2
    )


def idle():
    for frame in range(4):
        clear_canvas()
        warrior.clip_draw(225 + frame * 165, 839, 140, 140,
                          400, 300, 280, 280)
        update_canvas()
        delay(0.2)


def walk():
    for frame in range(8):
        clear_canvas()
        warrior.clip_draw(195 + frame * 165, 649, 140, 150,
                          400, 300, 280, 300)
        update_canvas()
        delay(0.2)


def run():
    for frame in range(6):
        clear_canvas()
        warrior.clip_draw(195 + frame * 165, 454, 150, 155,
                          400, 300, 300, 310)
        update_canvas()
        delay(0.2)


def attack():
    for frame in range(4):
        clear_canvas()
        warrior.clip_draw(205 + frame * 246, 274, 240, 155,
                          400, 300, 480, 310)
        update_canvas()
        delay(0.2)


def attack2():
    # The last row has uneven spacing; align each frame by the character.
    frame_x = (205, 451, 645, 891)
    for x in frame_x:
        clear_canvas()
        warrior.clip_draw(x, 94, 210, 150,
                          400, 300, 420, 300)
        update_canvas()
        delay(0.2)


while(True):
    idle()
    walk()
    run()
    attack()
    attack2()
