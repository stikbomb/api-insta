import requests


def fetch_hubble_images(url):

    response = requests.get(url)
    response.raise_for_status()
    image_url = 'https:{}'.format(response.json()['image_files'][-1]['file_url'])

    return image_url
