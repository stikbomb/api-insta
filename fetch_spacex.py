import requests


def fetch_spacex_launch(url):

    response = requests.get(url)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr_images']

    return images_urls
