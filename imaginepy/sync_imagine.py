import hashlib
import re
from enum import Enum
from typing import Union

import httpx
from langdetect import detect
from httpx import Response
from requests_toolbelt import MultipartEncoder

from .constants import *
from .exceptions import *
from .utils import *
import pybase64


class DeviantArt(Enum):
    ID = 23185
    SECRET = "fae0145a0736611056a5196a122c0d36"


class Imagine:

    def __init__(self, restricted: bool = True):
        self.restricted = restricted
        self.api = "https://inferenceengine.vyro.ai"
        self.cdn = "https://1966211409.rsc.cdn77.org/appStuff/imagine-fncisndcubnsduigfuds"
        self.version = 1

    def _request(self, **kwargs) -> Response:
        headers = {"accept": "*/*", "user-agent": "okhttp/4.10.0"}
        headers.update(kwargs.get("headers") or {})

        data = clear_dict(kwargs.get("data"))
        if data:
            prompt = data.get("prompt", "").lower().split(" ")
            if prompt:
                for i, word in enumerate(prompt):
                    word = re.sub(r'[^a-zA-Z]', "", word)
                    if word in BANNED_WORDS:
                        if self.restricted:
                            raise InvalidWord(f"Banned word found: {word}")
                        else:
                            prompt[i] = prompt[i].replace(word, get_word(word))

                data["prompt"] = " ".join(prompt)

            # any to str
            data = {key: str(value) if type(value) !=
                    tuple else value for key, value in data.items()}

            multi = MultipartEncoder(fields=data)
            headers["content-type"] = multi.content_type
            data = multi.read()

        try:
            with httpx.Client() as client:
                r = client.request(
                    method=kwargs.get("method", "GET"),
                    url=kwargs.get("url"),
                    data=data,
                    headers=headers,
                    timeout=60
                )
                r.raise_for_status()
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

        signature = hashlib.md5(r.content).hexdigest()
        if signature == "d8b21a024d6267f3014d874d8372f7c8":
            raise BannedContent("Violation of community guidelines.")
        return r

    def thumb(self, item: Union[Model, Style, Inspiration, Mode]) -> bytes:
        href = item.value[2 if isinstance(
            item, Model) or isinstance(item, Style) else 1]
        with httpx.Client() as client:
            response = client.get(f"{self.cdn}/{href}")
            response.raise_for_status()
            return bytes2png(response.content)

    def sdinsp(self, inspiration: Inspiration = Inspiration.INSPIRATION_01) -> bytes:
        """Inspiration"""
        return self.sdprem(
            prompt=inspiration.value[0],
            model=next(
                (item for item in Model if item.value[0] == inspiration.value[2]), Model.V3),
            seed=inspiration.value[3])

    def variate(
            self,
            content: bytes,
            prompt: str,
            model: Model = Model.V3,
            strength: int = 0,
            style: Style = None,
            asbase64: bool = False
    ) -> bytes:
        """Character"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/variate",
                data={
                    "model_version": self.version,
                    "prompt": prompt + (style.value[3] if style else ""),
                    "strength": strength,
                    "style_id": style.value[0] if style else model.value[0],
                    "image": ("image.jpeg", content, "image/jpg")
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def sdprem(
            self,
            prompt: str,
            negative: str = None,
            model: Model = Model.V3,
            style: Style = None,
            seed: int = None,
            ratio: Ratio = Ratio.RATIO_1X1,
            cfg: float = 9.5,
            priority: bool = True,
            high_result: bool = True,
            steps: int = 26,
            asbase64: bool = False
    ) -> bytes:
        """AI Art"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/sdprem",  # /sdprem (premium), /sd (free)
                data={
                    "model_version": self.version,
                    "prompt": prompt + (style.value[3] if style else ""),
                    "style_id": style.value[0] if style else model.value[0],
                    "aspect_ratio": ratio.value,
                    "seed": seed,
                    "cfg": get_cfg(cfg),
                    "negative_prompt": negative,
                    "priority": int(priority),
                    "high_res_results": int(high_result),
                    "steps": get_steps(steps)
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def upscale(self, content: bytes, asbase64: bool = False) -> bytes:
        """Upscale"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/upscale",
                data={
                    "model_version": self.version,
                    "image": ("_", content, "image/jpg")
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def translate(self, prompt: str) -> str:
        """Translate Prompt"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/translate",
                data={
                    "q": prompt,
                    "source": detect(prompt),
                    "target": "en"
                }
            )
            response_json = response.json()
            return response_json["translatedText"]
        except (httpx.RequestError, KeyError) as e:
            raise Exception(f"Request failed: {e}")

    def interrogator(self, content: bytes) -> str:
        """Generate Prompt"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/interrogator",
                data={
                    "model_version": self.version,
                    "image": ("prompt_generator_temp.jpeg", content, "image/jpg")
                }
            )
            return response.text
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def sdimg(
            self,
            content: bytes,
            mask: bytes,
            prompt: str,
            negative: str = None,
            seed: int = None,
            cfg: float = 9.5,
            priority: bool = True,
            asbase64: bool = False
    ) -> bytes:
        """Inpainting"""
        if not same_size(content, mask):
            raise InvalidSize("Mask size must be same as image size.")

        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/sdimg",
                data={
                    "model_version": self.version,
                    "prompt": prompt,
                    "negative_prompt": negative,
                    "seed": seed,
                    "cfg": get_cfg(cfg),
                    "image": ("temp_646.912234613557.jpg", content, "image/jpg"),
                    "mask": ("temp_646.912234613557.jpg", mask, "image/jpg"),
                    "priority": int(priority)
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def controlnet(
            self,
            content: bytes,
            prompt: str,
            model: Model = Model.V3,
            negative: str = None,
            strength: int = 0,
            cfg: float = 9.5,
            mode: Mode = Mode.SCRIBBLE,
            style: Style = None,
            seed: str = None,
            asbase64: bool = False
    ) -> bytes:
        """Image Remix"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/controlnet",
                data={
                    "model_version": self.version,
                    "prompt": prompt + (style.value[3] if style else ""),
                    "negative_prompt": negative,
                    "strength": strength,
                    "cfg": get_cfg(cfg),
                    "control": mode.value[0],
                    "style_id": style.value[0] if style else model.value[0],
                    "seed": seed,
                    "image": ("temp_314.1353898439128.jpg", content, "image/jpg")
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")

    def codeformer(self, content: bytes, asbase64: bool = False) -> bytes:
        """Face Fixed"""
        try:
            response = self._request(
                method="POST",
                url=f"{self.api}/codeformer",
                data={
                    "model_version": self.version,
                    "image": ("tempImage.jpg", content, "image/jpg")
                }
            )
            if asbase64 == True:
                return pybase64.b64encode(response.content).decode('utf-8')
            else:
                return bytes2png(response.content)
        except httpx.RequestError as e:
            raise Exception(f"Request failed: {e}")
