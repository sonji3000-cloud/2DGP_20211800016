from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')
boy = load_image('animation_sheet.png')
# fill here
frame = 0
action = 1
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
(left, bottom, width, height) = (0, 0, 100, 100)

while True:
    action = 1
    for x in range(0, 800, 5):
        clear_canvas()
        left = frame * FRAME_WIDTH
        bottom = action * FRAME_HEIGHT
        grass.draw(400, 30)
        boy.clip_draw(left, bottom, width, height, x, 90)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.05)
    delay(0.5)
    action = 0
    for x in range(750, 0, -5):
        clear_canvas()
        left = frame * FRAME_WIDTH
        bottom = action * FRAME_HEIGHT
        grass.draw(400, 30)
        boy.clip_draw(left, bottom, width, height, x, 90)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.05)

close_canvas()

