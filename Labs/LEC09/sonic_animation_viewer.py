"""소닉 스프라이트 시트의 모든 동작을 순서대로 재생한다."""

from pathlib import Path

from pico2d import *
IMAGE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SHEET_WIDTH = 399
SHEET_HEIGHT = 525
SCALE = 4
FRAME_SECONDS = 0.1
REPEAT_COUNT = 5


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
    ("동작 08 · 8행", row_frames(326, 370, (
        (1, 24),
        (31, 59),
        (65, 84),
        (90, 114),
        (119, 143),
        (149, 168),
        (184, 223),
        (232, 270),
    ))),
    ("동작 09 · 9행", row_frames(377, 416, (
        (1, 27),
        (31, 61),
        (64, 94),
        (99, 131),
        (136, 167),
        (176, 208),
        (217, 249),
        (254, 286),
    ))),
    ("동작 10 · 10행", row_frames(426, 468, (
        (6, 39),
        (49, 82),
        (96, 118),
        (125, 147),
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


def validate_animations():
    """동작 수와 잘못 잘린 프레임을 실행 전에 검사한다."""
    if len(ANIMATIONS) != 10:
        raise ValueError("소닉 동작이 10종이어야 합니다.")
    if sum(len(frames) for _, frames in ANIMATIONS) != 76:
        raise ValueError("소닉 프레임이 총 76개여야 합니다.")
    for name, frames in ANIMATIONS:
        if not frames:
            raise ValueError(f"{name}에 프레임이 없습니다.")
        for left, bottom, width, height in frames:
            if not (0 <= left < SHEET_WIDTH and 0 <= bottom < SHEET_HEIGHT):
                raise ValueError(f"{name}의 프레임 시작점이 시트 밖입니다.")
            if not (0 < width <= SHEET_WIDTH - left and 0 < height <= SHEET_HEIGHT - bottom):
                raise ValueError(f"{name}의 프레임 크기가 시트를 벗어납니다.")


def play_animation(sheet, frames):
    """동작의 프레임을 순서대로 표시한다."""
    for _ in range(REPEAT_COUNT):
        for frame in frames:
            draw_frame(sheet, frame)
            delay(FRAME_SECONDS)


def main():
    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(IMAGE_PATH)
    validate_animations()
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sheet = load_image(str(IMAGE_PATH))
        if (sheet.w, sheet.h) != (SHEET_WIDTH, SHEET_HEIGHT):
            raise ValueError("스프라이트 시트 크기가 399×525px이어야 합니다.")
        play_animation(sheet, ANIMATIONS[0][1])
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
