<div align="center">

<img src="./docs/imagine_logo.gif" width="10%">

**ImaginePy**

<img src="https://img.shields.io/badge/python-3.7+-informational?style=plastic" alt="Python version">
<img src="https://img.shields.io/github/release-date/hyugogirubato/pyImagine?style=plastic" alt="Release">
<img src="https://img.shields.io/github/release/hyugogirubato/pyImagine?style=plastic" alt="Version">
</div>

## Features

- 🎨 Turn words into art
- 👓 Choose from an array of art styles
- 🔧 Adjust your masterpiece with creative controls!
- 📦 Stay ahead of the game with the ever-growing art library!
- 🌇 Generate wallpapers
- 🔎 Discover and explore similar artistic designs

## Installation

_Note: Requires [Python] 3.7.0 or newer with PIP installed._

```shell
$ python setup.py install
```

You now have the `imaginepy` package installed.

### From Source Code

The following steps are instructions on download, preparing, and running the code under a Venv environment.
You can skip steps 3-5 with a simple `python setup.py install` call instead, but you miss out on a wide array of benefits.

1. `git clone https://github.com/hyugogirubato/pyImagine`
2. `cd pyImagine`
3. `python -m venv env`
4. `source env/bin/activate`
5. `python setup.py install`

As seen in Step 5, running the `pyimagine` executable is somewhat different to a normal PIP installation.
See [Venv's Docs] on various ways of making calls under the virtual-environment.

[Python]: https://python.org
[Venv's]: https://docs.python.org/3/tutorial/venv.html
[Venv's Docs]: https://docs.python.org/3/library/venv.html

## Usage

The following is a minimal example of using pyImagine in a script. It gets the generated image
from the text and increases the quality.

```python
from pyimagine import Imagine, Style, Ratio

def main():
    imagine = Imagine()

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

## Credit

- Imagine Icon &copy; Vyro AI
- Original reverse and version by: [hyugogirubato]: <https://github.com/hyugogirubato/pyImagine>

## License

[GNU General Public License, Version 3.0](LICENSE)
