<div align="center">
<b>>PyPi IS NOT UPDATE! PLEASE INSTALL FROM THE REPO!</b>
<br>
  
<img src="https://github.com/ItsCEED/ImaginePy-Midjourney-Free-Alternative/blob/main/docs/imagine_logo.gif" width="10%">

**ImaginePy**
<br>
<a href="https://discord.gg/axfkjqWR5E" target="_blank">
  <img src="https://discordapp.com/api/guilds/1110314971012808774/widget.png?style=banner4" alt="Discord Banner 4">
</a>
<br>
<img src="https://img.shields.io/badge/python-3.7+-informational?style=plastic" alt="Python version">
<img src="https://img.shields.io/github/release-date/ItsCEED/ImaginePy-Midjourney-Free-Alternative?style=plastic" alt="Release">
<img src="https://img.shields.io/github/release/ItsCEED/ImaginePy-Midjourney-Free-Alternative?style=plastic" alt="Version">

</div>

## Features

- 🎨 Turn words into art
- 👓 Choose from an array of art styles
- 🔧 Adjust your masterpiece with creative controls!
- 📦 Stay ahead of the game with the ever-growing art library!
- 🌇 Generate wallpapers
- 🔎 Discover and explore similar artistic designs
- This is refactored and improved version of the original from [hyugogirubato]

## Installation

_Note: Requires [Python] 3.7.0 or newer with PIP installed._

```shell
$ python setup.py install
```

You now have the `imaginepy` package installed.

### PyPi Installation

```
pip install imaginepy
```

[Python]: https://python.org
[Venv's]: https://docs.python.org/3/tutorial/venv.html
[Venv's Docs]: https://docs.python.org/3/library/venv.html
[hyugogirubato]: https://github.com/hyugogirubato/pyImagine

### From Source Code

The following steps are instructions on download, preparing, and running the code under a Venv environment.
You can skip steps 3-5 with a simple `python setup.py install` call instead, but you miss out on a wide array of benefits.

1. `git clone https://github.com/ItsCEED/Imaginepy`
2. `cd Imaginepy`
3. `python -m venv env`
4. `source env/bin/activate`
5. `python setup.py install`

As seen in Step 5, running the `imaginepy` executable is somewhat different to a normal PIP installation.
See [Venv's Docs] on various ways of making calls under the virtual-environment.

[Python]: https://python.org
[Venv's]: https://docs.python.org/3/tutorial/venv.html
[Venv's Docs]: https://docs.python.org/3/library/venv.html
[hyugogirubato]: https://github.com/hyugogirubato/pyImagine

## Usage

The following is a minimal example of using ImaginePy in a script. It gets the generated image
from the text and increases the quality.

```python
from imaginepy import Imagine, Style, Ratio

def main():
    imagine = Imagine(style=Style.ANIME_V2)

    img_data = imagine.sdprem(
        prompt="Woman sitting on a table, looking at the sky, seen from behind",
        style=Style.ANIME_V2,
        ratio=Ratio.RATIO_16X9
    )

    if img_data is None:
        print("An error occurred while generating the image.")
        return

    img_data = imagine.upscale(image=img_data)

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
```

Async version

```python
import asyncio
from imaginepy import AsyncImagine, Style, Ratio


async def main():
    imagine = AsyncImagine(style=Style.ANIME_V2)

    img_data = await imagine.sdprem(
        prompt="Woman sitting on a table, looking at the sky, seen from behind",
        style=Style.ANIME_V2,
        ratio=Ratio.RATIO_16X9
    )

    if img_data is None:
        print("An error occurred while generating the image.")
        return

    img_data = await imagine.upscale(image=img_data)

    if img_data is None:
        print("An error occurred while upscaling the image.")
        return

    await imagine.close()
    try:
        with open("example.png", mode="wb") as img_file:
            img_file.write(img_data)
    except Exception as e:
        print(f"An error occurred while writing the image to file: {e}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Credit

- Imagine Icon &copy; Vyro AI & API
- Original reverse and version by: [hyugogirubato]

## License

[GNU General Public License, Version 3.0](LICENSE)
