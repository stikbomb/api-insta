import os
import json
import argparse

import requests

from service_tools import get_file_extension, save_image


def fetch_spacex_launch():

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Url of spacex start')
    parser.add_argument('--filename', help='Filename mask for output file. Default - "spacex"', default='spacex')
    parser.add_argument('--path', help='Path to save file. Default - "./images/"', default='./images/')

    args = parser.parse_args()

    url = args.url
    path_to_images = args.path
    filename_mask = args.filename

    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)

    response = requests.get(url)
    response.raise_for_status()
    images_urls = json.loads(response.content)['links']['flickr_images']
    for image_id, image_url in enumerate(images_urls, start=1):

        extension = get_file_extension(image_url)

        filename = filename_mask + '-' + str(image_id) + '.' + extension
        full_path = path_to_images + filename

        save_image(full_path, image_url)


fetch_spacex_launch()
