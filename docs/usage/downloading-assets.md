# ⬇ Downloading assets

{% hint style="info" %}
There is no real use of this unless you need the images.
{% endhint %}

```python
from imaginepy import Imagine, Style

imagine = Imagine()

# Iterate over all styles
for style in Style:
    try:
        assets_data = imagine.assets(style)

        file_path = f"assets/{style.value[1]}.webp"
        with open(file_path, "wb") as file:
            file.write(assets_data)

        print(f"Downloaded assets for style: {style.value[1]}")
    except Exception as e:
        print(
            f"Error occurred while downloading assets for style {style.value[1]}: {e}")

print("Asset download completed.")
```
