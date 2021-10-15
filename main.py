from typing import Optional

from fastapi import FastAPI
from xaitk_saliency import PerturbImage
import PIL.Image
from PIL import Image
import urllib.request


app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/imageurl")
def read_image_size(image_url: str):
    try:
       image = Image.open(urllib.request.urlopen(image_url))
       return {"Width": image.size[0], "Height": image.size[1], "Format": image.format}
    except:
        return {"Error": "incorrecturl"}