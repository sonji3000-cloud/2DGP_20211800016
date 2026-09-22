from math import cos, sin, pi, hypot, ceil
from pathlib import Path

from pico2d import (
    open_canvas, close_canvas, load_image,
    clear_canvas, update_canvas, delay, get_events,
    SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE,
)


WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH / 2, HEIGHT / 2
RADIUS = 200
STEP = 2  # 한 프레임에 이동할 거리 (픽셀)
FRAME_DELAY = 0.01


def circle_points():
    # 오른쪽 끝에서 출발하여 반시계 방향으로 한 바퀴 돈다.
    frames = ceil(2 * pi * RADIUS / STEP)
    for i in range(frames + 1):
        angle = 2 * pi * i / frames
        yield (
            CENTER_X + RADIUS * cos(angle),
            CENTER_Y + RADIUS * sin(angle),
        )


def polygon_points(vertices):
    # 마지막 꼭짓점에서 첫 꼭짓점으로 돌아와 도형을 완주한다.
    for index, start in enumerate(vertices):
        end = vertices[(index + 1) % len(vertices)]
        dx, dy = end[0] - start[0], end[1] - start[1]
        frames = max(1, ceil(hypot(dx, dy) / STEP))
        for i in range(1, frames + 1):
            t = i / frames
            yield start[0] + dx * t, start[1] + dy * t


def motion_points():
    # 모든 경로를 (600, 300)에서 시작하고 끝내어 전환 시 연결한다.
    rectangle = [(600, 300), (600, 500), (200, 500),
                 (200, 100), (600, 100)]
    triangle = [(600, 300), (300, 500), (300, 100)]
    while True:
        yield from circle_points()
        yield from polygon_points(rectangle)
        yield from polygon_points(triangle)


def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        # 실행한 폴더와 관계없이 이 파일 옆의 이미지를 읽는다.
        image_path = Path(__file__).resolve().with_name('character.png')
        character = load_image(str(image_path))

        for x, y in motion_points():
            for event in get_events():
                if event.type == SDL_QUIT:
                    return
                if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    return

            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(FRAME_DELAY)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
