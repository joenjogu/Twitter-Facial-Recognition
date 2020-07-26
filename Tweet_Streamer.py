import tweepy
import json

# KENYA_COUNTRY_ID = "17ad6a68301cd28b"

class MyTweetStreamer(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me 

    def on_status(self, tweet):
        print(f"{tweet.user.name} says {tweet.text} \n")

    def on_error(self, status):
        print("Error")

# listener = MyTweetStreamer(api)
# stream = tweepy.Stream(api.auth, listener)
# stream.filter(track=["mastingo"], is_async=True)

