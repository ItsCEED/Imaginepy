from langdetect import detect
import aiohttp
import io

from .constants import *


def validate_cfg(cfg: float) -> str:
    """Validates the cfg parameter."""
    if cfg < 0.0 or cfg > 16.0:
        raise ValueError(f"Invalid CFG, must be in range (0; 16), {cfg}")
    return str(cfg)


class AsyncImagine:
    """Async class for handling API requests to the Imagine service."""

    HEADERS = {
        "accept": "*/*",
        "user-agent": "okhttp/4.10.0"
    }

    def __init__(self, style: Style = Style.IMAGINE_V1):
        self.asset = "https://1966211409.rsc.cdn77.org"
        self.api = "https://inferenceengine.vyro.ai"
        if style is not None:
            self.HEADERS["style-id"] = str(style.value[0]) # accepts as string
        self.session = aiohttp.ClientSession(raise_for_status=True, headers=self.HEADERS)
        self.version = "1"

    async def close(self) -> None:
        """Close async session"""
        return await self.session.close()

    def get_style_url(self, style: Style = Style.IMAGINE_V1) -> str:
        """Get link of style thumbnail"""
        return f"{self.asset}/appStuff/imagine-fncisndcubnsduigfuds//assets/{style.value[2]}/{style.value[1]}.webp"
    
    def bytes_to_io(self, data:bytes, filename:str) -> io.BytesIO:
        """Convert bytes to io.BytesIO with name for sending"""
        bio = io.BytesIO(data)
        bio.name=filename
        return bio
    
    async def assets(self, style: Style = Style.IMAGINE_V1) -> bytes:
        """Gets the assets."""
        try:
            async with self.session.get(
                url=self.get_style_url(style=style)
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while retrieving assets: {e}")

    async def variate(self, image: bytes, prompt: str, style: Style = Style.IMAGINE_V1) -> bytes:
        try:
            async with self.session.post(
                    url=f'{self.api}/variate',
                    data={
                        "model_version": self.version,
                        "prompt": prompt + (style.value[3] or ""),
                        "strength": "0",
                        "style_id": str(style.value[0]),
                        "image": self.bytes_to_io(image, "image.png")
                    }
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while making variations: {e}")
    async def sdprem(self, prompt: str, negative: str = None, priority: str = None, steps: str = None, high_res_results: str = None, style: Style = Style.IMAGINE_V1, seed: str = None, ratio: Ratio = Ratio.RATIO_1X1, cfg: float = 9.5) -> bytes:
        """Generates AI Art."""
        try:
            validated_cfg = validate_cfg(cfg)
        except Exception as e:
            raise ValueError(f"An error occurred while validating cfg: {e}")

        try:
            async with self.session.post(
                    url=f"{self.api}/sdprem",
                    data={
                        "model_version": self.version,
                        "prompt": prompt + (style.value[3] or ""),
                        "negative_prompt": negative or "",
                        "style_id": style.value[0],
                        "aspect_ratio": ratio.value,
                        "seed": seed or "",
                        "steps": steps or "30",
                        "cfg": validated_cfg,
                        "priority": priority or "0",
                        "high_res_results": high_res_results or "0"
                    }
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while making the request: {e}")

    async def upscale(self, image: bytes) -> bytes:
        """Upscales the image."""
        try:
            async with self.session.post(
                    url=f"{self.api}/upscale",
                    data={
                        "model_version": self.version,
                        "image": self.bytes_to_io(image, "test.png")
                    }
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while making upscale request: {e}")


    async def translate(self, prompt: str) -> str:
        """Translates the prompt."""
        try:
            async with self.session.post(
                    url=f"{self.api}/translate",
                    data={
                        "q": prompt,
                        "source": detect(prompt),
                        "target": "en"
                    }
                ) as resp:
                return (await resp.json())["translatedText"]
        except Exception as e:
            raise ConnectionError(f"An error occurred while translating the prompt: {e}")

    async def interrogator(self, image: bytes) -> str:
        """Generates a prompt."""
        try:
            async with self.session.post(
                    url=f"{self.api}/interrogator",
                    data={
                        "model_version": str(self.version),
                        "image": self.bytes_to_io(image,"prompt_generator_temp.png")
                    }
                ) as resp:
                return await resp.text()
        except Exception as e:
            raise ConnectionError(f"An error occurred while generating a prompt: {e}")

    async def sdimg(self, image: bytes, prompt: str, negative: str = None, seed: str = None, cfg: float = 9.5) -> bytes:
        """Performs inpainting."""
        try:
            async with self.session.post(
                    url=f"{self.api}/sdimg",
                    data={
                        "model_version": self.version,
                        "prompt": prompt,
                        "negative_prompt": negative or "",
                        "seed": seed or "",
                        "cfg": validate_cfg(cfg),
                        "image": self.bytes_to_io(image, "image.png")
                    }
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while performing an inpainting: {e}")


    async def controlnet(self, image: bytes, prompt: str, negative: str = None, cfg: float = 9.5, control: Control = Control.SCRIBBLE, style: Style = Style.IMAGINE_V1, seed: str = None) -> bytes:
        """Performs image remix."""
        try:
            async with self.session.post(
                    url=f"{self.api}/controlnet",
                    data={
                        "model_version": self.version,
                        "prompt": prompt + (style.value[3] or ""),
                        "negative_prompt": negative or "",
                        "strength": "0",
                        "cfg": validate_cfg(cfg),
                        "control": control.value,
                        "style_id": str(style.value[0]),
                        "seed": seed or "",
                        "image": self.bytes_to_io(image, "image.png")
                    }
                ) as resp:
                return await resp.read()
        except Exception as e:
            raise ConnectionError(f"An error occurred while image remixing: {e}")

