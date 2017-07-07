import tweepy


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def tweet(post):
    cfg = {
        "consumer_key": "XXXxxxxxXXxxxxxxxXXXXxxxxxx",
        "consumer_secret": "XXXxxxxxXXxxxxxxxXXXXxxxxxxXXXxxxxxXXxxxxxxxXXXXxxxxxx",
        "access_token": "YYYYyyyYYyyyyyyyyyyYYYYYYYYYyy",
        "access_token_secret" : "YYYYyyyYYyyyyyyyyyyYYYYYYYYYyyYYYYyyyYYyyyyyyyyyyYYYYYYYYYyy"
        }

    api = get_api(cfg)
    tweet = post
    status = api.update_status(status=tweet)

