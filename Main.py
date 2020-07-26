from Url_Retriever import GetTweetMediaUrl
from Image_Downloader import download_image_from_url
from facial_recognition import tagFaces

getter = GetTweetMediaUrl(1287096429056610304)

photo_urls = getter.get_urls()

download_image_from_url(photo_urls)

