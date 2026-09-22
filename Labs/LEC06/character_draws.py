# 실습 과제 진행
from math import pi, cos, sin
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')
center_x, center_y = 400, 300
radius = 200
x, y = center_x, center_y

def move_circle():
    angle = 0
    print("circle")
    while angle < 2 * pi:
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
        angle += 0.01
    # 원을 움직이는 코드 작성
    pass

def move_rectangle():
    # 사각형을 움직이는 코드 작성
    print("rectangle")
    for y in range(300, 501, 5):
        x = 600
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    for x in range(600, 199, -5):
        y = 500
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    for y in range(500, 299, -5):
        x = 200
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    pass

def move_triangle():
    # 삼각형을 움직이는 코드 작성
    print("triangle")
    pass


while True:
    update_canvas()
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()
