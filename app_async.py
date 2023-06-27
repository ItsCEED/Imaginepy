import asyncio
from imaginepy import AsyncImagine, Style, Ratio, Model, constants


async def main():
    imagine = AsyncImagine()
    img_data = await imagine.sdprem(
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

    img_data = await imagine.upscale(content=img_data)

    if img_data is None:
        print("An error occurred while upscaling the image.")
        return

    try:
        with open("example.png", mode="wb") as img_file:
            img_file.write(img_data)
    except Exception as e:
        print(f"An error occurred while writing the image to file: {e}")


if __name__ == "__main__":
    asyncio.run(main())
