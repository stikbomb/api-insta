import argparse

import requests


def get_file_extension(path):
    file_extension = path.split('.')[-1]
    return file_extension


def save_image(path, url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'script',
        help='Script to run. pti - publish to instagram, fs - fetch spacex, fh - fetch hubble',
        choices=['pti', 'fs', 'fh']
    )
    parser.add_argument('-u', '--url', help='Url of image to download')
    parser.add_argument('-p', '--path', help='Path to save file. Default - "./images/"', default='./images/')

    args = parser.parse_args()
    return args
