import os

import dotenv

from publish_to_instagram import publish_images
from fetch_spacex import fetch_spacex_launch
from fetch_hubble import fetch_hubble_images
from service_tools import parse_args, get_file_extension, save_image


class NoURLException(BaseException):
    pass


def main():
    dotenv.load_dotenv()

    args = parse_args()

    if args.script == 'pti':
        publish_images(args.path)

    if args.script == 'fs':
        if args.url is None:
            raise NoURLException('Scripts "ft" and "fs" need URL argument')
        images_urls = fetch_spacex_launch(args.url)

        for image_id, image_url in enumerate(images_urls, start=1):
            extension = get_file_extension(image_url)

            full_path = f'{args.path}spacex-{image_id}.{extension}'

            os.makedirs(args.path, exist_ok=True)
            save_image(full_path, image_url)

    if args.script == 'fh':
        if args.url is None:
            raise NoURLException('Scripts "ft" and "fs" need URL argument')
        image_url = fetch_hubble_images(args.url)

        extension = get_file_extension(image_url)
        full_path = f'{args.path}hubble.{extension}'

        os.makedirs(args.path, exist_ok=True)
        save_image(full_path, image_url)


if __name__ == '__main__':
    main()
