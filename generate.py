import subprocess
import sys
import os

def install(packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

# Example usage:
packages = ['imaginepy', 'tk', 'ttkthemes', 'aiohttp', 'pybase64']
install(packages)

print("Finished installing requirements.")


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from imaginepy import Imagine
from imaginepy.constants import *
import os
import random
import string
import webbrowser
import threading
import platform

imagine = Imagine()

models = [
    "V4_CREATIVE", "IMAGINE_V1", "IMAGINE_V3", "IMAGINE_V4_Beta", "ANIME", "PORTRAIT", "REALISTIC" 
]

styles = [
    "ABSTRACT_CITYSCAPE", "ABSTRACT_VIBRANT", "AMAZONIAN", "ANIME_V2", "ARCHITECTURE", "AVATAR",
    "CANDYLAND", "CLAYMATION", "CINEMATIC_RENDER", "COMIC_BOOK", "COMIC_V2",
    "COSMIC", "CUBISM", "DISNEY", "DYSTOPIAN", "ELVEN", "EUPHORIC", "EXTRA_TERRESTRIAL", "FANTASY", "FIREBENDER",
    "FORESTPUNK", "FUTURISTIC", "GLASS_ART", "GHOTIC", "GRAFFITI", "GTA", "HAUNTED", "ICON", "ILLUSTRATION",
    "INTERIOR", "JAPANESE_ART", "KAWAII_CHIBI", "KNOLLING_CASE",
    "LANDSCAPE", "LOGO", "MACRO_PHOTOGRAPHY", "MARBLE", "MEDIEVAL", "MINECRAFT", "MYSTICAL", "NEO_FAUVISM", 
    "NEON", "ORIGAMI", "PAINTING", "PALETTE_KNIFE", "PAPERCUT_STYLE", "PICASO", "PIXEL_ART", 
    "POLAROID", "POLY_ART", "POP_ART", "POSTER_ART", "PRODUCT_PHOTOGRAPHY", 
    "PSYCHEDELIC", "RAINBOW", "RENDER", "RENAISSANCE", "RETRO", "RETROWAVE", "ROCOCCO",
    "SAMURAI", "SCATTER", "SHAMROCK_FANTASY", "SKETCH", "STAINED_GLASS", "STICKER", "STUDIO_GHIBLI", 
    "SURREALISM", "VAN_GOGH", "VIBRANT", "VIBRAN_VIKING", "WATERBENDER", "WOOLITIZE"
]

ratios = [
    "RATIO_1X1", "RATIO_2X3", "RATIO_3X1", "RATIO_3X2", "RATIO_3X4", "RATIO_4X3", "RATIO_4X5",
    "RATIO_5X4", "RATIO_9X16", "RATIO_16X9"
]



def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def browse_images():
    open_image_folder()

def open_image(path):
    if platform.system() == "Windows":
        os.startfile(path)
    else:
        subprocess.call(['xdg-open', path])

def open_image_folder():
    if platform.system() == "Windows":
        os.startfile("images")
    elif platform.system() == "Darwin":
        subprocess.call(('open', 'images'))
    else:  # Linux variants
        subprocess.call(('xdg-open', 'images'))

def generate_image():
    progress_win = Toplevel(root)
    progress_win.geometry('200x100')

    # Center the progress_win with respect to the root window
    window_width = progress_win.winfo_reqwidth()
    window_height = progress_win.winfo_reqheight()
    position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    progress_win.geometry("+{}+{}".format(position_right, position_top))

    progress_lbl = Label(progress_win, text="Generating image...")
    progress_lbl.pack(pady=20)
    progress_bar = ttk.Progressbar(progress_win, mode='indeterminate', length=280)  # Adjust the length parameter
    progress_bar.pack(padx=20)
    progress_bar.start()

    # Run the image generation in a separate thread
    def generate():
        prompt = entry.get()
        style_str = style_cbox.get()
        ratio_str = ratio_cbox.get()
        model_str = model_cbox.get()

        # Map string back to Enum value
        style_enum = next((s for s in Style if s.name == style_str), Style.NO_STYLE)
        ratio_enum = next((r for r in Ratio if r.name == ratio_str), Ratio.RATIO_16X9)
        model_enum = next((m for m in Model if m.name == model_str), Model.REALISTIC)

        cfg_value = int(cfg_scale.get())

        negative_str = negative_entry.get()

        img_data = imagine.sdprem(
            prompt=prompt,
            style=style_enum,
            ratio=ratio_enum,
            negative=negative_str,  # Use the entered negative string
            seed=1000,
            cfg=cfg_value,
            model=model_enum,
            asbase64=False
        )

        img_data = imagine.upscale(img_data)

        # Save as PNG with a random name
        img_filename = random_string(10) + '.png'
        img_path = os.path.join('images', img_filename)

        try:
            with open(img_path, mode="wb") as img_file:
                img_file.write(img_data)
        except Exception as e:
            print(f"An error occurred while writing the image to file: {e}")

        img = Image.open(img_path)
        img.thumbnail((700, 700), Image.LANCZOS)  # Resize keeping aspect ratio
        img = ImageTk.PhotoImage(img)

        lbl.config(image=img)
        lbl.image = img  # keep a reference!
        lbl.bind("<Button-1>", lambda e: open_image(img_path))  # Open image in default viewer

        progress_win.destroy()

    threading.Thread(target=generate).start()

root = ThemedTk(theme="ubuntu")
root.title("MakuluLinux 4K Image Generator")

# For PNG file
icon = PhotoImage(file='text-image.png')
root.iconphoto(False, icon)

# Calculate position of main window to center on screen
window_width = 1080
window_height = 750
position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


frame = ttk.Frame(root)
frame.place(x=0, y=0, width=1080, height=750)

prompt_lbl = ttk.Label(frame, text="Input:", font=("Arial", 12))  # Increase font size to 14
prompt_lbl.place(x=10, y=15)

entry = ttk.Entry(frame, width=50, font=("Arial", 16))  # Increase font size to 12
entry.place(x=70, y=10)

negative_lbl = ttk.Label(frame, text="Negative:", font=("Arial", 12))  # Increase font size to 14
negative_lbl.place(x=705, y=15)  # Adjust the position as per your layout

negative_entry = ttk.Entry(frame, width=20, font=("Arial", 16))  # Increase font size to 12
negative_entry.place(x=800, y=10)  # Adjust the position as per your layout

model_lbl = ttk.Label(frame, text="Model:", font=("Arial", 12))  # Increase font size to 14
model_lbl.place(x=10, y=65)

model_cbox = ttk.Combobox(frame, values=models, state='readonly', font=("Arial", 12))  # Increase font size to 12
model_cbox.set("IMAGINE_V3")  # Set default model
model_cbox.place(x=70, y=60)

style_lbl = ttk.Label(frame, text="Style:", font=("Arial", 12))  # Increase font size to 14
style_lbl.place(x=10, y=125)

style_cbox = ttk.Combobox(frame, values=styles, state='readonly', font=("Arial", 12))  # Increase font size to 12
style_cbox.set("ANIME_V2")  # Set default style
style_cbox.place(x=70, y=120)

ratio_lbl = ttk.Label(frame, text="Ratio:", font=("Arial", 12))  # Increase font size to 14
ratio_lbl.place(x=10, y=185)

ratio_cbox = ttk.Combobox(frame, values=ratios, state='readonly', font=("Arial", 12))  # Increase font size to 12
ratio_cbox.set("RATIO_16X9")  # Set default ratio
ratio_cbox.place(x=70, y=180)

# Add this before the "Generate" button
cfg_lbl = ttk.Label(frame, text="<--- Higher Quality | Better Prompt --->", font=("Arial", 12))  # Increase font size to 14
cfg_lbl.place(x=30, y=250)

cfg_scale = ttk.Scale(frame, from_=3, to=15, orient=HORIZONTAL, length=200)  # Adjust the length parameter
cfg_scale.set(3)  # Set default value
cfg_scale.place(x=70, y=290)

btn_style = ttk.Style()
btn_style.configure("Custom.TButton", font=("Arial", 18))  # Set the font for the custom style
btn = ttk.Button(frame, text="Generate", command=generate_image, width=12, style="Custom.TButton")  # Use the custom style
btn.place(x=60, y=340)

browse_btn = ttk.Button(frame, text="Browse", command=browse_images, width=12, style="Custom.TButton")  # Increase font size to 14
browse_btn.place(x=60, y=400)

lbl = ttk.Label(frame)
lbl.place(x=320, y=120)

root.mainloop()
