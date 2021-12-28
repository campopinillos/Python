
import twitter, re, datetime, pandas as pd

class twitterminer():
    request_limit = 20
    api             =   False
    data            =   []
    twitter_keys = {
        'consumer_key': 'WqCOsLCeJHrtNfLPckOzG3DKR', #add your consumer key
        'consumer_secret': '9MaIElyoxkP1cPcTLxyEwv0dLtzZRTc6CGXsvfU6nlfWU7Kk2g', #add your consumer secret key
        'access_token_key': '1076189593500897280-tXvEpCzD5UCMXefFT5OwpkwF1cFwA4', #add your access token key
        'access_token_secret':  'H1n5ymNddskJT8bpAAUKtpanCtSSG1bV4rhckyDnutsoX', #add your access token secret key
        'bearer_token': 'AAAAAAAAAAAAAAAAAAAAACKtIQEAAAAARdOX8x76V3rcVgWY7ocvg%2FT51J8%3DIPIWeohELStn5WQjo8suKYSfMg7hLYQP46m1kosHKPNNLjKjIa' #add your bearer token
    }
    
    
    def __init__(self,  request_limit = 20):
        self.request_limit = request_limit
        
        # This sets the twitter API object for use internall within the class
        self.set_api()
    
    def set_api(self):
        self.api = twitter.Api(
            consumer_key         =   self.twitter_keys['consumer_key'],
            consumer_secret      =   self.twitter_keys['consumer_secret'],
            access_token_key     =   self.twitter_keys['access_token_key'],
            access_token_secret  =   self.twitter_keys['access_token_secret'])
    # def auth():
    #     return os.environ.get("BEARER_TOKEN")

    def mine_user_tweets(self, user=" set default user to get data from", mine_retweets=False):
        statuses   =   self.api.GetUserTimeline(screen_name=user, count=self.request_limit)
        data       =   []
            
        for item in statuses:
            mined = {
                'tweet_id': item.id,
                'handle': item.user.name,
                'retweet_count': item.retweet_count,
                'text': item.text,
                'mined_at': datetime.datetime.now(),
                'created_at': item.created_at}
            data.append(mined)
                
        return data

    def mine_user_followers(self, user=" set default user to get data from", mine_retweets=False):
        statuses   =   self.api.GetFollowers(screen_name=user, count=self.request_limit)
        data       =   []
            
        for item in statuses:
            mined = {item}
            data.append(mined)
                
        return data



mine = twitterminer()

# insert handle we like
tweets = mine.mine_user_tweets("@AlvaroUribeVel")

foll = mine.mine_user_followers("@AlvaroUribeVel")
df = pd.DataFrame(tweets)
df2 = pd.DataFrame(foll)
df.head()
df2.head()
print(os.environ.get("BEARER_TOKEN"))






from twitter import *

twitter_keys = {
        'consumer_key': 'WqCOsLCeJHrtNfLPckOzG3DKR', #add your consumer key
        'consumer_secret': '9MaIElyoxkP1cPcTLxyEwv0dLtzZRTc6CGXsvfU6nlfWU7Kk2g', #add your consumer secret key
        'access_token_key': '1076189593500897280-tXvEpCzD5UCMXefFT5OwpkwF1cFwA4', #add your access token key
        'access_token_secret':  'H1n5ymNddskJT8bpAAUKtpanCtSSG1bV4rhckyDnutsoX', #add your access token secret key
        'bearer_token': 'AAAAAAAAAAAAAAAAAAAAACKtIQEAAAAARdOX8x76V3rcVgWY7ocvg%2FT51J8%3DIPIWeohELStn5WQjo8suKYSfMg7hLYQP46m1kosHKPNNLjKjIa' #add your bearer token
    }

consumer_key         =   twitter_keys['consumer_key'],
consumer_secret      =   twitter_keys['consumer_secret'],
token     =   twitter_keys['access_token_key'],
token_secret  =   twitter_keys['access_token_secret']
BEARER_TOKEN = twitter_keys['bearer_token']


t = Twitter(auth=OAuth2(bearer_token=BEARER_TOKEN))



t = twitter.Api(token, token_secret, consumer_key, consumer_secret)

t.GetFollowers


t.GetFollowers(screen_name=("@AlvaroUribeVel"), count=100)