import os
import shutil

import requests


def get_cat(folder, name):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_image_from_url(url)
    save_image(folder, name, data)


def get_image_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder,name,data):
    filename = os.path.join(folder, name)
    with open(filename, 'wb') as f:
        shutil.copyfileobj(data, f)
