import requests

def download_image_from_url(photo_url_list):
    for index, photo_url in enumerate(photo_url_list):
        with open(f'photo{index}.jpg', 'wb') as handle:
                response = requests.get(photo_url, stream=True)

                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)