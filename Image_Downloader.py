import requests
import os
import random
import time

def download_image_from_url(photo_url_list):
    path = os.path.join(f"{os.getcwd()}","Downloaded_Images")
    if not os.path.exists(path):
        os.mkdir(path)

    for index, photo_url in enumerate(photo_url_list):
        start_time = time.clock()
        with open(f'{path}\photo{random.randint(0,1000)}.jpg', 'wb') as handle:
                response = requests.get(photo_url, stream=True)

                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
                process_time = time.clock() - start_time
                print(f"Downloaded Image {index + 1} of {len(photo_url_list)} in {process_time:.3f} seconds")