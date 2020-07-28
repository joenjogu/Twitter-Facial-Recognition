import tweepy
import time

def create_api():
    start_time = time.clock()
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
    process_time = time.clock() - start_time
    print(f"API Auth took {process_time} seconds")
    return api 