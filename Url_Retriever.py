from create_api import create_api

class GetTweetMediaUrl():
    api = create_api()

    def __init__(self, status):
        self.status = status

    def get_tweet(self):
        try:
            tweet = self.api.get_status(self.status)
        except Exception as e:
            raise e
        return tweet

    def get_media_url(self, tweet):
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

    def get_urls(self):
        tweet = self.get_tweet()
        return self.get_media_url(tweet)