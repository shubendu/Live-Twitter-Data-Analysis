import os
import tweepy as tw
import pandas as pd

#put your api keys and tokens here
# API Keys and Tokens
consumer_key= '################################'
consumer_secret= '################################'
access_token= '################################'
access_token_secret= '################################'

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":


    #ref: https://github.com/tweepy/tweepy/issues/974
    first_100_joe = []
    query = "#JoeBiden"
    for tweet_info in tweepy.Cursor(api.search, q=query, lang = 'en', tweet_mode='extended').items(170):
        if 'retweeted_status' in dir(tweet_info):
            tweet=tweet_info.retweeted_status.full_text
            first_100_joe.append(tweet)
    else:
        tweet=tweet_info.full_text
        first_100_joe.append(tweet)

    first_100_joe = pd.DataFrame(first_100_joe[:100])
    #saving it to txt file
    first_100_joe.to_csv('first_100_joe.txt', index=None, header = None, sep='\n', mode='a')
