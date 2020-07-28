from Url_Retriever import GetTweetMediaUrl
from Image_Downloader import download_image_from_url
from tweet_scraper import get_status_ids
from facial_recognition import tagFaces
from create_api import create_api

getter = GetTweetMediaUrl(
    get_status_ids(create_api(),"2015vs2020", 100)
    )

photo_urls = getter.get_urls()
download_image_from_url(photo_urls)
tagFaces("C:\\Users\\JOE\JOB\Twitter Facial Recognition\\Downloaded_Images")
