import random
from io import BytesIO

from PIL import Image


def bytes2png(content: bytes) -> bytes:
    # Convert the image to PNG format
    src_image = Image.open(BytesIO(content))
    png_image = src_image.convert("RGBA")

    # Save the PNG image to bytes
    png_data = BytesIO()
    png_image.save(png_data, format="PNG")
    png_data.seek(0)
    return png_data.getvalue()


def clear_dict(value: dict) -> dict:
    return {key: value for key, value in value.items() if value is not None} if value else None


def get_cfg(value: float) -> float:
    if value < 0.0 or value > 16.0:
        raise ValueError(f"Invalid CFG, must be in range (0; 16), {value}")
    return value


def get_steps(value: int) -> int:
    if value < 0 or value > 50:
        raise ValueError(f"Invalid steps, must be in range (0; 50), {value}")
    return value


def get_word(value: str) -> str:
    chars = list(value.lower())
    size = len(chars) - 1
    vowel = chars[0] in "aeiouy"

    for i in range(size + 1):
        if i > 0 and chars[i] == chars[i - 1]:
            chars.insert(i + 1, chars[i])
            return "".join(chars)
        if i == size // 2 and size % 2 == 1:
            chars.insert(i + 1, chars[i])
            return "".join(chars)

    if vowel:
        chars.insert(2, chars[1])
    else:
        i = random.randint(0, size)
        chars.insert(i + 1, chars[i])
    return "".join(chars)


def same_size(src1: bytes, src2: bytes) -> bool:
    width1, height1 = Image.open(BytesIO(src1)).size
    width2, height2 = Image.open(BytesIO(src2)).size
    return width1 == width2 and height1 == height2
