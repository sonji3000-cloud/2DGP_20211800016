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
        draw_frame(sheet, (1, 447, 29, 39))
        delay(1.0)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
