import tweepy
import time

def create_api():
    start_time = time.clock()       

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

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