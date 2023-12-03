# A Python program to set the desktop background image to a new picture every
# day using the NASA Astronomy Picture Of the Day API
#
# @author Clayton Whitten
# @version 1.2

import ctypes
import os
from PIL import Image
import requests

# returns the byte data of the astronomy picture of the day image
def get_apod_image():
    data = requests.get(
        url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&thumbs=True"
    ).json()

    if "thumbnail_url" in data:
        data_url = data['thumbnail_url']
    else:
        data_url = data['url']

    image_data = requests.get(data_url).content
    return image_data

# writes image byte data into jpg file
apod = get_apod_image()
try:
    with open(rf'{os.getcwd()}\apod.jpg', 'wb') as handler:
        handler.write(apod)
except Exception as e:
    print(f"Error writing to 'apod.jpg': {e}")

# resizes the image to standard 1920x1080
apod_img = Image.open('apod.jpg')
(width, height) = apod_img.size
left = int((width - 1920)/2)
right = left + 1920
resized_img = apod_img.crop((left, 0, right, height))
resized_img = resized_img.resize((1920, height))
resized_img.save('apod.jpg')

# sets the desktop background image
SPI_SETDESKWALLPAPER = 20
apod_path = rf"{os.getcwd()}\apod.jpg"
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, apod_path, 3)