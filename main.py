# A Python program to set the desktop background image to a new picture every
# day using the NASA Astronomy Picture Of the Day API
#
# @author Clayton Whitten
# @version 1.0

import ctypes
from PIL import Image
import requests

# returns the byte data of the astronomy picture of the day image
def get_apod_image():
    data_url = requests.get(
        url=f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    ).json()['url']

    image_data = requests.get(data_url).content
    return image_data

# writes image byte data into jpg file
apod = get_apod_image()
with open('apod.jpg', 'wb') as handler:
    handler.write(apod)

# resizes the image to standard 1920x1080
correct_fit_apod = Image.open('apod.jpg')
(width, height) = correct_fit_apod.size
left = int((width - 1920)/2)
right = left + 1920
new_img = correct_fit_apod.crop((left, 0, right, height))
new_img = new_img.resize((1920, 1080))
new_img.save('apod.jpg', quality=95)

# sets the desktop background image
SPI_SETDESKWALLPAPER = 20
apod_path = r"C:\Users\Stash\PycharmProjects\AstronomyDesktop\apod.jpg"
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, apod_path, 3)