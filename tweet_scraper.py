import tweepy

def get_status_ids(api, search_term, items):
    status_ids = []
    
    for tweet in tweepy.Cursor(api.search,\
        q= search_term, 
        ).items(items):
        status_ids.append(tweet.id)

    return status_ids
