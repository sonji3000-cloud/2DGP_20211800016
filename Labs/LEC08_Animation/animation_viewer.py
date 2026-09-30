from pico2d import *

open_canvas()

warrior = load_image('WarriorSprite.png')


def draw_frame(left, bottom, width, height):
    warrior.clip_draw(
        left, bottom, width, height,
        400, 300, width * 2, height * 2
    )


def play_frame(left, bottom, width, height):
    clear_canvas()
    draw_frame(left, bottom, width, height)
    update_canvas()
    delay(0.2)


def idle():
    for frame in range(4):
        play_frame(225 + frame * 165, 839, 140, 140)

def walk():
    for frame in range(8):
        play_frame(195 + frame * 165, 649, 140, 150)


def run():
    for frame in range(6):
        play_frame(195 + frame * 165, 454, 150, 155)


def attack():
    for frame in range(4):
        play_frame(205 + frame * 246, 274, 240, 155)


def attack2():
    frame_x = (205, 451, 645, 891)
    for x in frame_x:
        clear_canvas()
        draw_frame(x, 94, 210, 150)
        update_canvas()
        delay(0.2)


while(True):
    for animation in (idle, walk, run, attack, attack2):
        for repeat in range(5):
            animation()
        delay(1.0)
