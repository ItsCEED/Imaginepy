from enum import Enum
from typing import Any, Optional, Tuple
from requests import Session, Response
from requests_toolbelt.multipart.encoder import MultipartEncoder
from langdetect import detect

class Style(Enum):
    """
    Enumeration class for different styles. Each style has three attributes:
    - style_id: Identifier for the style.
    - asset: Reference to the asset associated with the style.
    - suffix: Additional descriptor that can be appended to a prompt when using the style.
    """
    IMAGINE_BETA = (30, "Imagine_V3.5", None)
    IMAGINE_V3 = (28, "thumbv1_27", ", 4k, high quality, hdr")
    IMAGINE_V1 = (27, "thumbv1_28", None)
    REALISM = (29, "thumbv1_29", None)
    ANIME_STYLE = (21, "thumb_20", None)
    COSMIC = (28, "thumb-01", "in cosmic atmosphere, humanitys cosmic future,  space art concept, space landscape, scene in space, cosmic space, beautiful space star planet, background in space, realistic, cinematic, breathtaking view")
    MARBLE = (28, "thumb-02", "in greek marble style, classical antiquities, ancient greek classical ancient greek art, marble art, realistic, cinematic")
    MINECRAFT = (28, "thumb-03", "minecraft build, style of minecraft, pixel style, 8 bit, epic, cinematic, screenshot from minecraft, detailed natural lighting, minecraft gameplay, mojang,  minecraft mods, minecraft in real life,  blocky like minecraft")
    DISNEY = (28, "thumb-04", "disney animation, disney splash art, disney color palette, disney renaissance film, disney pixar movie still, disney art style, disney concept art :: nixri, wonderful compositions, pixar, disney concept artists, 2d character design")
    MACRO_PHOTOGRAPHY = (28, "thumb-05", "macro photography, award winning macro photography, depth of field, extreme closeup, 8k hd, focused")
    GTA = (28, "thumb-06", "gta iv art style, gta art,  gta loading screen art, gta chinatowon art style, gta 5 loading screen poster, grand theft auto 5, grand theft auto video game")
    STUDIO_GHIBLI = (28, "thumb-07", "studio ghibli movie still, ghibli screenshot, joe hisaishi, makoto shinkai, cinematic studio ghibli still, fantasy art landscape, whimsical, dreamlike, anime beautiful peace scene, studio ghibli painting, cinematic")
    DYSTOPIAN = (28, "thumb-08", "cifi world, cybernetic civilizations, peter gric and dan mumford,   brutalist dark futuristic, dystopian brutalist atmosphere, dark dystopian world, cinematic 8k, end of the world, doomsday")
    STAINED_GLASS = (28, "thumb-09", "intricate wiccan spectrum, stained glass art, vividly beautiful colors, beautiful stained glass window, colorful image, intricate stained glass triptych, gothic stained glass style, stained glass window!!!")
    PRODUCT_PHOTOGRAPHY = (28, "thumb-10", "product photo studio lighting,  high detail product photo, product photography, commercial product photography, realistic, light, 8k, award winning product photography, professional closeup")
    PSYCHEDELIC = (28, "thumb-11", "psychedelic painting, psychedelic dripping colors, colorful detailed projections, android jones and chris dyer, psychedelic vibrant colors, intricate psychedelic patterns, psychedelic visuals, hallucinatory art")
    SURREALISM = (28, "thumb-12", "salvador dali painting, highly detailed surrealist art, surrealist conceptual art,  masterpiece surrealism, surreal architecture, surrealistic digital artwork, whimsical surrealism, bizarre art")
    GRAFFITI = (28, "thumb-13", "graffiti background, colorful graffiti, graffiti art style, colorful mural, ravi supa, symbolic mural, juxtapoz, pablo picasso, street art")
    GOTHIC = (28, "thumb-14", "goth lifestyle, dark goth, grunge, cinematic photography, dramatic dark scenery, dark ambient beautiful")
    RAINBOW = (28, "thumb-15", "intricate rainbow environment, rainbow bg, from lorax movie, pixar color palette, volumetric rainbow lighting, gorgeous digital painting, 8k cinematic")
    AVATAR = (28, "thumb-16", "avatar movie, avatar with blue skin, vfx movie, cinematic lighting, utopian jungle, pandora jungle, sci-fi nether world, lost world, pandora fantasy landscape,lush green landscape, high quality render")
    PALETTE_KNIFE = (28, "thumb-17", "detailed impasto brush strokes,  detail acrylic palette knife, thick impasto technique,  palette knife, vibrant 8k colors")
    CANDYLAND = (28, "thumb-18", "candy land style,  whimsical fantasy landscape art, japanese pop surrealism, colorfull digital fantasy art, made of candy and lollypops, whimsical and dreamy")
    CLAYMATION = (28, "thumb-19", "clay animation, as a claymation character, claymation style, animation key shot, plasticine, clay animation, stopmotion animation, aardman character design, plasticine models")
    EUPHORIC = (28, "thumb-20", "digital illustration, style of charlie bowater, dreamy colorful cyberpunk colors, euphoric fantasy, epic dreamlike fantasy landscape, beautiful oil matte painting, 8k fantasy art, fantasy art landscape, jessica rossier color scheme, dreamlike diffusion")
    MEDIEVAL = (28, "thumb-21", "movie still from game of thrones, powerful fantasy epic, middle ages, lush green landscape, olden times, roman empire, 1400 ce, highly detailed background, cinematic lighting, 8k render, high quality, bright colours")
    ORIGAMI = (28, "thumb-22", "polygonal art, layered paper art, paper origami, wonderful compositions, folded geometry, paper craft, made from paper")
    POP_ART = (28, "thumb-23", "pop art painting, detailed patterns pop art, silkscreen pop art, pop art poster, roy lichtenstein style")
    RENNAISANCE = (28, "thumb-24", "renaissance period, neo-classical painting, italian renaissance workshop, pittura metafisica, raphael high renaissance, ancient roman painting, michelangelo painting, Leonardo da Vinci, italian renaissance architecture")
    FANTASY = (28, "thumb-25", "fantasy matte painting,  fantasy landscape, ( ( thomas kinkade ) ), whimsical, dreamy, alice in wonderland, daydreaming, epic scene, high exposure, highly detailed, tim white, michael whelan")
    EXTRA_TERRES_TRIAL = (28, "thumb-26", "deepdream cosmic, painting by android jones, cosmic entity, humanoid creature, james jean soft light 4 k, sci fi, extra terrestrial, cinematic")
    WOOLITIZE = (28, "thumb-27", "cute! c4d, made out of wool, volumetric wool felting, wool felting art, houdini sidefx, rendered in arnold, soft smooth lighting, soft pastel colors")
    NEO_FAUVISM = (28, "thumb-28", "neo-fauvism painting, neo-fauvism movement, digital illustration, poster art, cgsociety saturated colors, fauvist")
    AMAZONIAN = (28, "thumb-29", "amazonian cave, landscape, jungle, waterfall, moss-covered ancient ruins, Dramatic lighting and intense colors, mesmerizing details of the environment and breathtaking atmosphere")
    SHAMROCK_FANTASY = (28, "thumb-30", "shamrock fantasy, fantasy, vivid colors, grapevine, celtic fantasy art, lucky clovers, dreamlike atmosphere, captivating details, soft light and vivid colors")
    ABSTRACT_VIBRANT = (28, "thumb-31", "vibrant, editorial, abstract elements, colorful, color splatter, realism, Inspired by the style of Ryan Hewett, dynamic realism, soft lighting and intricate details")
    NEON = (28, "thumb-32", "neon art style, night time dark with neon colors, blue neon lighting, violet and aqua neon lights, blacklight neon colors, rococo cyber neon lighting")
    CUBISM = (28, "thumb-33", "cubist picasso, cubism,  a cubist painting, heavy cubism, cubist painting, by Carlo Carrà, style of picasso, modern cubism, futuristic cubism")
    BAUHAUS = (28, "thumb-34", "Bauhaus art movement,  by Wassily Kandinsky, bauhaus style painting, geometric abstraction, vibrant colors, painting")
    ROCOCCO = (28, "thumb-35", "francois boucher oil painting, rococco style,  rococco lifestyle, a flemish Baroque, by Karel Dujardin, vintage look, cinematic hazy lighting")
    HUNTED = (28, "thumb-36", "horror cgi 4 k, scary color art in 4 k, horror movie cinematography, insidious, la llorona, still from animated horror movie, film still from horror movie, haunted, eerie, unsettling, creepy")
    LOGO = (28, "thumb-37", "creative logo, unique logo, visual identity, geometric type, graphic design, logotype design, brand identity, vector based, trendy typography, best of behance")
    WATERBENDER = (28, "thumb-38", "water elements, fantasy, water, exotic, A majestic composition with water elements, waterfall, lush moss and exotic flowers, highly detailed and realistic, dynamic lighting")
    FIREBENDER = (28, "thumb-39", "fire elements, fantasy, fire, lava, striking. A majestic composition with fire elements, fire and ashes surrounding, highly detailed and realistic, cinematic lighting")
    KAWAII_CHIBI = (28, "thumb-40", "kawaii chibi romance, fantasy, illustration, Colorful idyllic cheerful, Kawaii Chibi inspired")
    FORESTPUNK = (28, "thumb-41", "forestpunk, vibrant, HDRI, organic motifs and pollen in the air, bold vibrant colors and textures, spectacular sparkling rays, photorealistic quality with Hasselblad")
    ELVEN = (28, "thumb-42", "elven lifestyle, photoreal, realistic, 32k quality, crafted by Elves and engraved in copper, elven fantasy land, hyper detailed")
    SAMURAI = (28, "thumb-43", "samurai lifesyle, miyamoto musashi, Japanese art, ancient japanese samurai, feudal japan art, feudal japan art")
    AQUATIC = (28, "thumb-44", "graceful movement with intricate details, inspired by artists like Lotte Reiniger, Carne Griffiths and Alphonse Mucha. Dreamy and surreal atmosphere, twirling in an aquatic landscape with water surface")
    VIBRANT_VIKING = (28, "thumb-45", "Viking era, digital painting, pop of colour, forest, paint splatter, flowing colors, Background of lush forest and earthy tones, Artistic representation of movement and atmosphere")
    ABSTRACT_CITYSCAPE = (28, "thumb-46", "abstract cityscape, Ultra Realistic Cinematic Light abstract, futuristic, cityscape, Out of focus background and incredible 16k resolution produced in Unreal Engine 5 and Octan render")
    ILLUSTRATION = (28, "thumb_31", ", minimalistic vector art, illustrative style, style of ian hubert, style of gilles beloeil, inspired by Hsiao-Ron Cheng, style of jonathan solter, style of alexandre chaudret, by Echo Chernik")
    PAINTING = (28, "thumb_32", ", atmospheric dreamscape painting, by Mac Conner, vibrant gouache painting scenery, vibrant painting, vivid painting, a beautiful painting, dream scenery art, instagram art, psychedelic painting, lofi art, bright art")
    ICON = (28, "thumb_43", ", single vector graphics icon, ios icon, smooth shape, vector")
    RENDER = (28, "thumb_36", ", isometric, polaroid octane render, 3 d render 1 5 0 mm lens, keyshot product render, rendered, keyshot product render pinterest, 3 d product render, 3 d cgi render, 3d cgi render, ultra wide angle isometric view")
    LINE_ART = (28, "thumb_33", ", drawn with a single line, black and white, by Leila Faithfull, by Anne Ryan, by Hermione Hammond, by Amalia Lindegren, by Pamela Drew, by Louisa Puller, by Richard Benning, single line drawing, by Isobel Heath, one line artwork print, continuous line drawing, by Daniel Gelon")
    PAPERCUT_STYLE = (28, "thumb_39", ", layered paper art, paper modeling art, paper craft, paper art, papercraft, paper cutout, paper cut out collage artwork, paper cut art")
    KNOLLING_CASE = (28, "thumb_45", ", in  square glass case,  glass cube, glowing, knolling case, ash thorp, studio background,  desktopography, cgsociety 9,  cgsociety, mind-bending digital art")
    ANIME_V2 = (28, "thumb_37", ", anime atmospheric, atmospheric anime, anime character; full body art, digital anime art, beautiful anime art style, anime picture, anime arts, beautiful anime style, digital advanced anime art, anime painting, anime artwork, beautiful anime art, detailed digital anime art, anime epic artwork")
    PIXEL_ART = (28, "thumb_38", ", one pixel brush, pixelart, colorful pixel art")
    COMIC_V2 = (28, "thumb_34", ", comic book, john romita senior, inspired by Alton Tobey, by Alan Davis, arachnophobia, by Alton Tobey, as a panel of a marvel comic, marvel comic")
    INTERIOR = (28, "thumb_40", ", modern architecture by makoto shinkai, ilya kuvshinov, lois van baarle, rossdraws and frank lloyd wright")
    STICKER = (28, "thumb_35", ", sticker, sticker art, symmetrical sticker design, sticker - art, sticker illustration, die - cut sticker")
    CYBERPUNK = (28, "thumb_41", ", synthwave image, (neotokyo), dreamy colorful cyberpunk colors, cyberpunk blade runner art, retrofuturism, cyberpunk, beautiful cyberpunk style, cgsociety 9")
    LANDSCAPE = (28, "thumb_44", ", landscape 4k, beautiful landscapes, nature wallpaper, 8k photography")
    ARCHITECTURE = (28, "thumb_47", ", modern architecture design, luxury architecture, bright, very beautiful, trending on unsplash, breath taking")
    GLASS_ART = (28, "thumb_46", " inside glass ball, translucent sphere, cgsociety 9, glass orb, behance, polished, beautiful digital artwork, exquisite digital art, in a short round glass vase, octane render")
    SCATTER = (28, "thumb_42", ", breaking pieces, exploding pieces, shattering pieces,  disintegration, contemporary digital art, inspired by Dan Hillier, inspired by Igor Morski, dramatic digital art, behance art, cgsociety 9, 3d advanced digital art, mind-bending digital art, disintegrating")
    RETRO = (28, "thumb_30", ", retro futuristic illustration, featured on illustrationx, art deco illustration, beautiful retro art, stylized digital illustration, highly detailed vector art, ( ( mads berg ) ), automotive design art, epic smooth illustration, by mads berg, stylized illustration, ash thorp khyzyl saleem, clean vector art")
    POSTER_ART = (27, "thumb-56", ", album art, Poster, layout, typography, logo, risography, ghibili, simon stalenhag, insane detail, artstation, 8k")
    INK = (27, "thumb-50", ", Black Ink, Hand drawn, Minimal art, artstation, artgem, monochrome")
    JAPANESE_ART = (27, "thumb-51", ", Ukiyoe, illustration, muted colors")
    SALVADOR_DALI = (27, "thumb-58", ", Painting, by salvador dali, allegory, surrealism, religious art, genre painting, portrait, painter, still life")
    VAN_GOGH = (27, "thumb-61", ", painting, by van gogh")
    STEAMPUNK = (27, "thumb-60", " steampunk, stylized digital illustration, sharp focus, elegant, intricate, digital painting, artstation concept art, global illumination, ray tracing, advanced technology, chaykan howard, campion pascal, cooke darwin, davis jack, pink atmosphere")
    RETROWAVE = (27, "thumb-57", ", Illustration, retrowave art, noen light, retro, digital art, trending on artstation")
    PLOY_ART = (27, "thumb-55", ", low poly, artstation, studio lightning, stainless steel, grey color scheme")
    VIBRANT = (27, "thumb-62", ", Psychedelic, water colors spots, vibrant color scheme, highly detailed, romanticism style, cinematic, artstation, greg rutkowski")
    MYSTICAL = (27, "thumb-52", ", fireflies, deep focus, d&d, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, hearthstrom, gereg rutkowski, alphonse mucha, andreas rocha")
    CINEMATIC_RENDER = (27, "thumb-47", ", cinematic, breathtaking colors, close-up, cgscociety, computer rendering, by mike winkelmann, uhd, rendered in cinema4d, surface modeling, 8k, render octane, inspired by beksinski")
    FUTURISTIC = (27, "thumb-49", ", futuristic, elegant atmosphere, glowing lights, highly detailed, digital painting, artstation, concept art, smooth sharp focus, illustration, mars ravelo, gereg rutkowski")
    POLAROID = (27, "thumb-54", ", old polaroid, 35mm")
    PICASO = (27, "thumb-53", ", painting, by pablo picaso, cubism")
    SKETCH = (27, "thumb-59", ", pencil, hand drawn, sketch, on paper")
    COMIC_BOOK = (28, "thumb-48", ", Comic cover, 1960s marvel comic, comic book illustrations")

class Ratio(Enum):
    """Enum for the different image ratios."""
    RATIO_1X1 = (512, 512)
    RATIO_9X16 = (368, 648)
    RATIO_16X9 = (648, 368)
    RATIO_4X3 = (512, 384)
    RATIO_3X2 = (648, 432)

class Control(Enum):
    """Enum for the different controls."""
    SCRIBBLE = "scribble"
    POSE = "openpose"
    DEPTH = "depth"

class DeviantArt(Enum):
    """Enum for the DeviantArt API credentials."""
    ID = 23185
    SECRET = "fae0145a0736611056a5196a122c0d36"

def validate_cfg(cfg: float) -> str:
    """Validates the cfg parameter."""
    if cfg < 0.0 or cfg > 16.0:
        raise ValueError(f"Invalid CFG, must be in range (0; 16), {cfg}")
    return str(cfg)

class Imagine:
    """Class for handling API requests to the Imagine service."""

    HEADERS = {
        "accept": "*/*",
        "user-agent": "okhttp/4.10.0"
    }

    def __init__(self):
        self.asset = "https://1966211409.rsc.cdn77.org"
        self.api = "https://inferenceengine.vyro.ai"
        self.session = Session()
        self.version = "1"

    def _request(self, **kwargs) -> Response:
        """Sends a request to the server and returns the response."""
        headers = Imagine.HEADERS.copy()
        headers.update(kwargs.get("headers", {}))

        response = self.session.request(
            method=kwargs.get("method", "GET").upper(),
            url=kwargs.get("url"),
            params=kwargs.get("params"),
            data=kwargs.get("data"),
            headers=headers
        )
        response.raise_for_status()
        return response

    def _build_multipart_data(self, fields: dict) -> Tuple[MultipartEncoder, dict]:
        """Helper function to build multipart form data."""
        multi = MultipartEncoder(fields=fields)
        headers = {"content-type": multi.content_type}
        return multi, headers

    def assets(self, style: Style = Style.IMAGINE_V1) -> bytes:
        """Gets the assets."""
        return self._request(
            url=f"{self.asset}/appStuff/imagine-fncisndcubnsduigfuds//assets/styles_v4/{style.value[1]}.webp"
        ).content

    def variate(self, image: bytes, prompt: str, style: Style = Style.IMAGINE_V1) -> bytes:
        """Variates the character."""
        multi, headers = self._build_multipart_data({
            "model_version": self.version,
            "prompt": prompt + (style.value[2] or ""),
            "strength": "0",
            "style_id": str(style.value[0]),
            "image": ("image.jpeg", image, "image/jpeg")
        })
        
        return self._request(
            method="POST",
            url=f"{self.api}/variate",
            data=multi,
            headers=headers
        ).content

    def sdprem(self, prompt: str, negative: str = None, style: Style = Style.IMAGINE_V1, seed: str = None, ratio: Ratio = Ratio.RATIO_1X1, cfg: float = 9.5) -> bytes:
        """Generates AI Art."""
        try:
            validated_cfg = validate_cfg(cfg)
        except Exception as e:
            print(f"An error occurred while validating cfg: {e}")
            return None

        try:
            return self._request(
                method="POST",
                url=f"{self.api}/sdprem",
                data={
                    "model_version": self.version,
                    "prompt": prompt + (style.value[2] or ""),
                    "negative_prompt": negative or "",
                    "style_id": style.value[0],
                    "width": ratio.value[0],
                    "height": ratio.value[1],
                    "seed": seed or "",
                    "cfg": validated_cfg
                }
            ).content
        except Exception as e:
            print(f"An error occurred while making the request: {e}")
            return None

    def upscale(self, image: bytes) -> bytes:
        """Upscales the image."""
        try:
            multi, headers = self._build_multipart_data({
                "model_version": self.version,
                "image": ("test.jpeg", image, "image/jpeg")
            })
        except Exception as e:
            print(f"An error occurred while building the multipart data: {e}")
            return None

        try:
            return self._request(
                method="POST",
                url=f"{self.api}/upscale",
                data=multi,
                headers=headers
            ).content
        except Exception as e:
            print(f"An error occurred while making the request: {e}")
            return None


    def translate(self, prompt: str) -> str:
        """Translates the prompt."""
        multi, headers = self._build_multipart_data({
            "q": prompt,
            "source": detect(prompt),
            "target": "en"
        })

        return self._request(
            method="POST",
            url=f"{self.api}/translate",
            data=multi,
            headers=headers
        ).json()["translatedText"]

    def interrogator(self, image: bytes) -> str:
        """Generates a prompt."""
        multi, headers = self._build_multipart_data({
            "model_version": str(self.version),
            "image": ("prompt_generator_temp.jpeg", image, "application/zip")
        })

        return self._request(
            method="POST",
            url=f"{self.api}/interrogator",
            data=multi,
            headers=headers
        ).text

    def sdimg(self, image: bytes, prompt: str, negative: str = None, seed: str = None, cfg: float = 9.5) -> bytes:
        """Performs inpainting."""
        multi, headers = self._build_multipart_data({
            "model_version": self.version,
            "prompt": prompt,
            "negative_prompt": negative or "",
            "seed": seed or "",
            "cfg": validate_cfg(cfg),
            "image": ("image.jpeg", image, "image/jpeg")
        })

        return self._request(
            method="POST",
            url=f"{self.api}/sdimg",
            data=multi,
            headers=headers
        ).content

    def controlnet(self, image: bytes, prompt: str, negative: str = None, cfg: float = 9.5, control: Control = Control.SCRIBBLE, style: Style = Style.IMAGINE_V1, seed: str = None) -> bytes:
        """Performs image remix."""
        multi, headers = self._build_multipart_data({
            "model_version": self.version,
            "prompt": prompt + (style.value[2] or ""),
            "negative_prompt": negative or "",
            "strength": "0",
            "cfg": validate_cfg(cfg),
            "control": control.value,
            "style_id": str(style.value[0]),
            "seed": seed or "",
            "image": ("image.jpeg", image, "image/jpeg")
        })

        return self._request(
            method="POST",
            url=f"{self.api}/controlnet",
            data=multi,
            headers=headers
        ).content

__version__ = "1.0.1"