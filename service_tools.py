import requests


def get_file_extension(path):
    file_extension = path.split('.')[-1]
    return file_extension


def save_image(path, url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
