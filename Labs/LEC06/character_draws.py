# 실습 과제 진행
from math import pi, cos, sin
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')
center_x, center_y = 400, 300
radius = 200

def draw_boy(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.008)

def move_circle():
    angle = 0
    while angle < 2 * pi:
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        draw_boy(x, y)
        angle += 0.01

def move_right():
    for y in range(300, 501, 2):
        x = 600
        draw_boy(x, y)

def move_top():
    for x in range(600, 199, -2):
        y = 500
        draw_boy(x, y)

def move_left():
    for y in range(500, 299, -2):
        x = 200
        draw_boy(x, y)

def move_bottom():
    for x in range(200, 601, 2):
        y = 300
        draw_boy(x, y)

def move_rectangle():
    move_right()
    move_top()
    move_left()
    move_bottom()

def move_triangle():
    for i in range(201):
        x = 600 - i
        y = 300 + i
        draw_boy(x, y)
    for i in range(201):
        x = 400 - i
        y = 500 - i
        draw_boy(x, y)
    for x in range(200, 601, 2):
        y = 300
        draw_boy(x, y)


while True:
    move_circle()
    move_rectangle()
    move_triangle()
