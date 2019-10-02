import os
import glob
import time

from instabot import Bot
from PIL import Image


class InstagramResponseException(Exception):
    pass


def crop_image_to_square(path_with_filename):
    image = Image.open(path_with_filename)

    im_width = image.width
    im_height = image.height

    if im_width > im_height:
        coordinates = (
            (im_width - im_height) / 2,
            0,
            (im_width - im_height) / 2 + im_height,
            im_height)
    elif im_width < im_height:
        coordinates = (
            0,
            int((im_height - im_width) / 2),
            im_width,
            int((im_height - im_width) / 2 + im_width)
        )
    else:
        coordinates = (0, 0, im_width, im_height)

    cropped = image.crop(coordinates)

    cropped.save(path_with_filename)


def publish_one_image(path_with_filename):

    INSTA_LOGIN = os.getenv('INSTA_LOGIN')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')
    INSTABOT_SERVICE_PATH = './.instabot'

    bot = Bot(base_path=INSTABOT_SERVICE_PATH)
    bot.login(username=INSTA_LOGIN, password=INSTA_PASSWORD)

    crop_image_to_square(path_with_filename)

    filename = path_with_filename.split('/')[-1]

    bot.upload_photo(path_with_filename, caption=filename)

    if bot.api.last_response.status_code != 200:
        raise InstagramResponseException('Response status is not 200!')


def publish_images(path):

    path_to_images = f'{path}*'

    for image in glob.glob(path_to_images):
        publish_one_image(image)
        time.sleep(90)
