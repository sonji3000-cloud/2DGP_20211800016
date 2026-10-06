"""소닉 스프라이트 시트의 모든 동작을 순서대로 재생한다."""

from pathlib import Path

from pico2d import *
IMAGE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SHEET_WIDTH = 399
SHEET_HEIGHT = 525
SCALE = 4


def row_frames(top, bottom, spans):
    """시트 위쪽 기준 행 범위를 pico2d 프레임 좌표로 바꾼다."""
    height = bottom - top + 1
    return tuple(
        (left, SHEET_HEIGHT - bottom - 1, right - left + 1, height)
        for left, right in spans
    )


ANIMATIONS = (
    ("동작 01 · 1행", row_frames(39, 77, (
        (1, 29),
        (31, 56),
        (58, 86),
        (87, 115),
        (118, 147),
        (150, 179),
        (182, 210),
        (211, 239),
        (240, 268),
        (270, 293),
        (302, 330),
    ))),
    ("동작 02 · 2행", row_frames(79, 117, (
        (8, 33),
        (37, 63),
        (65, 95),
        (97, 133),
        (135, 166),
        (170, 201),
        (206, 231),
        (238, 261),
        (263, 292),
        (295, 330),
        (334, 365),
        (370, 398),
    ))),
    ("동작 03 · 3행", row_frames(121, 163, (
        (1, 33),
        (39, 73),
        (89, 123),
        (130, 163),
        (181, 214),
        (228, 260),
    ))),
    ("동작 04 · 4행", row_frames(167, 199, (
        (1, 29),
        (35, 63),
        (67, 96),
        (98, 128),
        (131, 159),
        (162, 190),
        (193, 222),
        (230, 260),
        (268, 297),
    ))),
    ("동작 05 · 5행", row_frames(206, 232, (
        (1, 30),
        (36, 64),
        (70, 98),
        (105, 133),
        (139, 167),
        (174, 202),
    ))),
    ("동작 06 · 6행", row_frames(238, 273, (
        (1, 29),
        (36, 65),
        (74, 104),
        (111, 141),
        (149, 178),
        (186, 216),
    ))),
    ("동작 07 · 7행", row_frames(283, 317, (
        (1, 29),
        (36, 65),
        (72, 110),
        (123, 161),
        (172, 210),
        (218, 255),
    ))),
)


def draw_frame(sheet, frame):
    """한 프레임을 화면 중앙에 원본 크기의 네 배로 그린다."""
    left, bottom, width, height = frame
    clear_canvas()
    sheet.clip_draw(
        left, bottom, width, height,
        CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
        width * SCALE, height * SCALE,
    )
    update_canvas()


def main():
    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(IMAGE_PATH)
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sheet = load_image(str(IMAGE_PATH))
        if (sheet.w, sheet.h) != (SHEET_WIDTH, SHEET_HEIGHT):
            raise ValueError("스프라이트 시트 크기가 399×525px이어야 합니다.")
        draw_frame(sheet, ANIMATIONS[0][1][0])
        delay(1.0)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
