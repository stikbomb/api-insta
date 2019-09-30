import os
import json
import argparse

import requests

from service_tools import get_file_extension, save_image


def fetch_hubble_images():

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Url of hubble image url')
    parser.add_argument('--filename', help='Filename mask for output file. Default - "hubble"', default='hubble')
    parser.add_argument('--path', help='Path to save file. Default - "./images/"', default='./images/')

    args = parser.parse_args()

    url = args.url
    path_to_images = args.path
    filename_mask = args.filename

    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)

    response = requests.get(url)
    response.raise_for_status()
    image_url = 'https:' + json.loads(response.content)['image_files'][-1]['file_url']

    extension = get_file_extension(image_url)
    filename = filename_mask + '.' + extension
    full_path = path_to_images + filename

    save_image(full_path, image_url)


fetch_hubble_images()
