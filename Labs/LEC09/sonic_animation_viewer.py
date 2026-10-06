"""소닉 스프라이트 시트의 모든 동작을 순서대로 재생한다."""

from pathlib import Path

from pico2d import *
IMAGE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")


def main():
    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(IMAGE_PATH)


if __name__ == "__main__":
    main()
