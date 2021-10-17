from typing import Optional
import numpy as np
from fastapi import FastAPI
from xaitk_saliency import PerturbImage
from xaitk_saliency.impls.perturb_image.sliding_window import SlidingWindow

from PIL import Image
import urllib.request


app = FastAPI()


#stored perturbed image from calling perturb image, filled after running perturb_image
perturbeddataarray = np.ndarray

#basic API call for troubleshooting
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#gets an image by url and returns basic data (dimensions and format)
@app.get("/imageurl")
def read_image_data(image_url: str):
    try:
       image = Image.open(urllib.request.urlopen(image_url))

       return {"Width": image.size[0], 
            "Height": image.size[1], 
            "Format": image.format}
    except:
        #there was an error getting the image
        return {"Error": "incorrecturl"}

#perturbs the image using the xaitk sliding window impl
@app.get("/perturb/sliding_window")
def perturb_image(image_url: str):
    #takes in an image from url and perturbs it, storing resulting masks 
    #in a ndarray of booleans (this will in turn be used in another call)
    try:
        #Getting the image
        image = Image.open(urllib.request.urlopen(image_url))
        #turning into numpy array, 3D array of ints
        ref_image = np.array(image)
        #creating a sliding window perturbation class
        slidingwindow = SlidingWindow()
        #perturbing the image, saving as 'perturbeddataarray'
        perturbeddataarray = slidingwindow.perturb(ref_image)
       
        return {"Successfully perturbed": 200}
        
    except:
        #error getting the image
        return {"ERROR": "url"}
