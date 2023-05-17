# 🖼 Generating an image

```python
from imaginepy import Imagine, Style, Ratio

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

    try:
        with open("example.png", mode="wb") as img_file:
            img_file.write(img_data)
    except Exception as e:
        print(f"An error occurred while writing the image to file: {e}")

if __name__ == "__main__":
    main()
```

#### Parameters for `sdprem` functions

```

"model_version": #It seems that is always 1
"prompt": #The prompt itself + Style Mods
"negative_prompt": #Negative Prompt
"style_id": #The id of the style
"width": #Width in pixels
"height": #Height in pixels
"seed": #A random number that can go up to 999999999
"cfg": #CFG scale adjusts how much the image will be like your prompt. Higher values keep your image
closer to your prompt.
Note: Higher values can reduce the output quality, giving less room to the Al for being creative.

"priority": #0 or 1, it should get you faster render
"high_res_results": #0 or 1, it should get you the maximum render res

```

>
