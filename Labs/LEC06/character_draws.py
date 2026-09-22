# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')
x, y = 400, 300

def move_circle():
    print("circle")
    clear_canvas()
    character.draw(x, y)
    # 원을 움직이는 코드 작성
    pass

def move_rectangle():
    # 사각형을 움직이는 코드 작성
    print("rectangle")
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
