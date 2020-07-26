import tweepy
import json

# KENYA_COUNTRY_ID = "17ad6a68301cd28b"

# class MyTweetStreamer(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me 

#     def on_status(self, tweet):
#         print(f"{tweet.user.name} says {tweet.text} \n")

#     def on_error(self, status):
#         print("Error")


def create_api():
    consumer_key= "f7mXFiU0ZhA2QpO2ci1sHTkrQ"
    consumer_secret = "WQUhp5mRWW1bcAx1Rmt8NN0KGEghGEKWAQjpNuEJFGvk41nwC0"
    access_token= "1078230130898714625-y3mJrVdCyn5Ii8VR8v8LrHdbypB17p"
    access_token_secret = "OV4V66kFPJQo4nLMvRwUbIOkgF3aEUV2oJFuUiXZiHnOn"        

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(
        auth, 
        wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True
        )

    try:
        api.verify_credentials()
    except Exception as e:
        raise e

    return api


def get_tweet(api, tweet_id):
    try:
        tweet = api.get_status(tweet_id)
    except Exception as e:
        raise e
    return tweet

def get_media_url(tweet):
    try:
        entities = tweet.extended_entities
        media_type = entities["media"][0]["type"]

        if media_type != "photo":
            pass
        else:
            try:
                media_urls = []
                for key in range(len(entities["media"])):
                    photo_url = entities["media"][key]["media_url"]
                    media_urls.append(photo_url)
                return (media_urls) 
            except IndexError as e:
                print ("Maximum photos reached...", e)
    except AttributeError as attribute_error: 
        print ("tweet has no media...", attribute_error) 


status_2015_2020 = 1285236694883561472
status_baby = 1286735937674907653

print (get_media_url(get_tweet(create_api(), status_baby)))




# listener = MyTweetStreamer(api)
# stream = tweepy.Stream(api.auth, listener)
# stream.filter(track=["mastingo"], is_async=True)

