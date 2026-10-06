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
PAUSE_SECONDS = 1.0
RENDER_SECONDS = 1.0 / 60.0
EDGE_MARGIN = 20


def row_frames(top, bottom, spans):
    """시트 위쪽 기준 행 범위를 pico2d 프레임 좌표로 바꾼다."""
    height = bottom - top + 1
    return tuple(
        (left, SHEET_HEIGHT - bottom - 1, right - left + 1, height)
        for left, right in spans
    )


# 원본 시트의 행별 좌표. 실제 재생 단위는 아래 ANIMATION_SPECS에서 나눈다.
SPRITE_ROWS = (
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


# (이름, 시트 행, 첫 프레임, 마지막 프레임, (가로 속도, 점프 높이)).
# 행과 프레임 번호는 1부터 시작하며 마지막 번호를 포함한다.
# 프레임 범위와 이동 설정을 함께 선언해 분할 시 설정이 밀리지 않게 한다.
ANIMATION_SPECS = (
    ("대기", 1, 1, 7, (0, 0)),
    ("대기 별도 동작", 1, 8, 11, (0, 0)),
    ("달리기", 2, 1, 12, (240, 0)),
    ("질주", 3, 1, 6, (0, 0)),
    ("회전 진입", 4, 1, 9, (0, 0)),
    ("구르기", 5, 1, 6, (220, 0)),
    ("회전 달리기", 6, 1, 6, (260, 0)),
    ("고속 회전 달리기", 7, 1, 6, (340, 0)),
    ("점프", 8, 1, 6, (0, 0)),
    ("공중 자세", 8, 7, 8, (0, 0)),
    ("걷기 변형", 9, 1, 8, (0, 0)),
    ("포즈 A", 10, 1, 2, (0, 0)),
    ("포즈 B", 10, 3, 4, (0, 0)),
)

ANIMATIONS = tuple(
    (name, SPRITE_ROWS[row - 1][1][first - 1:last])
    for name, row, first, last, _ in ANIMATION_SPECS
)
MOTIONS = tuple(motion for _, _, _, _, motion in ANIMATION_SPECS)


def motion_pose(frames, motion, elapsed):
    """실제 경과 시간으로 위치와 방향을 계산한다. 큰 시간 간격도 반사한다."""
    speed, jump_height = motion
    half_width = max(frame[2] for frame in frames) * SCALE / 2
    left_edge = EDGE_MARGIN + half_width
    right_edge = CANVAS_WIDTH - EDGE_MARGIN - half_width
    span = right_edge - left_edge
    distance = (CANVAS_WIDTH / 2 - left_edge + speed * elapsed) % (2 * span)
    facing_right = distance < span
    x = left_edge + (distance if facing_right else 2 * span - distance)
    cycle_seconds = len(frames) * FRAME_SECONDS
    phase = (elapsed % cycle_seconds) / cycle_seconds
    y = CANVAS_HEIGHT / 2 + 4 * jump_height * phase * (1 - phase)
    return x, y, facing_right


def draw_frame(sheet, frame, pose):
    """현재 위치와 진행 방향에 맞춰 프레임을 네 배로 그린다."""
    left, bottom, width, height = frame
    x, y, facing_right = pose
    clear_canvas()
    sheet.clip_composite_draw(
        left, bottom, width, height,
        0, '' if facing_right else 'h', x, y,
        width * SCALE, height * SCALE,
    )
    update_canvas()


def validate_animations():
    """동작 수와 잘못 잘린 프레임을 실행 전에 검사한다."""
    for name, row, first, last, _ in ANIMATION_SPECS:
        if not (1 <= row <= len(SPRITE_ROWS)
                and 1 <= first <= last <= len(SPRITE_ROWS[row - 1][1])):
            raise ValueError(f"{name}의 원본 프레임 범위가 잘못되었습니다.")
    if len(MOTIONS) != len(ANIMATIONS):
        raise ValueError("각 동작에 이동 설정이 하나씩 있어야 합니다.")
    if sum(len(frames) for _, frames in ANIMATIONS) != 76:
        raise ValueError("소닉 프레임이 총 76개여야 합니다.")
    source_frames = {frame for _, frames in SPRITE_ROWS for frame in frames}
    playback_frames = {frame for _, frames in ANIMATIONS for frame in frames}
    if len(source_frames) != 76 or playback_frames != source_frames:
        raise ValueError("분리된 동작에 누락되거나 중복된 프레임이 있습니다.")
    for name, frames in ANIMATIONS:
        if not frames:
            raise ValueError(f"{name}에 프레임이 없습니다.")
        for left, bottom, width, height in frames:
            if not (0 <= left < SHEET_WIDTH and 0 <= bottom < SHEET_HEIGHT):
                raise ValueError(f"{name}의 프레임 시작점이 시트 밖입니다.")
            if not (0 < width <= SHEET_WIDTH - left and 0 < height <= SHEET_HEIGHT - bottom):
                raise ValueError(f"{name}의 프레임 크기가 시트를 벗어납니다.")


def wait_with_events(seconds):
    """지정 시간 동안 종료 이벤트를 계속 처리한다."""
    deadline = get_time() + seconds
    while True:
        for event in get_events():
            if event.type == SDL_QUIT:
                return False
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                return False
        remaining = deadline - get_time()
        if remaining <= 0:
            return True
        delay(min(0.01, remaining))


def play_animation(sheet, frames, motion):
    """프레임 전환과 이동을 함께 갱신하고 마지막 화면을 유지한다."""
    started = get_time()
    frame_count = len(frames) * REPEAT_COUNT
    duration = frame_count * FRAME_SECONDS
    while True:
        if not wait_with_events(0):
            return False
        elapsed = min(get_time() - started, duration)
        frame_index = min(int(elapsed / FRAME_SECONDS), frame_count - 1)
        pose = motion_pose(frames, motion, elapsed)
        draw_frame(sheet, frames[frame_index % len(frames)], pose)
        if elapsed >= duration:
            break
        delay(min(RENDER_SECONDS, duration - elapsed))
    # 재생이 끝난 위치·방향·마지막 프레임을 그대로 유지한다.
    return wait_with_events(PAUSE_SECONDS)


def validate_display_bounds():
    """모든 확대 프레임이 캔버스 안에 들어가는지 확인한다."""
    for (name, frames), (speed, jump_height) in zip(ANIMATIONS, MOTIONS):
        if speed < 0 or jump_height < 0:
            raise ValueError(f"{name}의 이동 속도와 점프 높이는 음수일 수 없습니다.")
        for _, _, width, height in frames:
            if (width * SCALE + 2 * EDGE_MARGIN >= CANVAS_WIDTH
                    or height * SCALE / 2 + jump_height > CANVAS_HEIGHT / 2):
                raise ValueError(f"{name}의 프레임이 캔버스를 벗어납니다.")


def main():
    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(IMAGE_PATH)
    validate_animations()
    validate_display_bounds()
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sheet = load_image(str(IMAGE_PATH))
        if (sheet.w, sheet.h) != (SHEET_WIDTH, SHEET_HEIGHT):
            raise ValueError("스프라이트 시트 크기가 399×525px이어야 합니다.")
        while True:
            for (_, frames), motion in zip(ANIMATIONS, MOTIONS):
                if not play_animation(sheet, frames, motion):
                    return
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
