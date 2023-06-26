from imaginepy import Imagine
from imaginepy.constants import *


def main():
    imagine = Imagine()

    img_data = imagine.sdprem(
        prompt="Woman sitting on a table, looking at the sky, seen from behind",
        style=Style.NO_STYLE,
        ratio=Ratio.RATIO_16X9,
        negative="",
        seed=1000,
        cfg=16,
        model=Model.REALISTIC,
        asbase64=False  # default is false, putting it here as presentation.
    )

    if img_data is None:
        print("An error occurred while generating the image.")
        return

    img_data = imagine.upscale(img_data)

    if img_data is None:
        print("An error occurred while upscaling the image.")
        return

    try:
        with open("example.jpeg", mode="wb") as img_file:
            img_file.write(img_data)
    except Exception as e:
        print(f"An error occurred while writing the image to file: {e}")


if __name__ == "__main__":
    main()
