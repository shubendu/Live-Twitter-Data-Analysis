import tweepy
import os
import json
import sys
import geocoder

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

    #woeid of India
    woeid = 23424848
  
    # fetching the trends
    trends = api.trends_place(id = woeid, include = '#')
    
    #creating two lists to store the topics and thier count
    topics = []
    no_of_topics = []
  
    for value in trends: 
        for trend in value['trends']:
            #storing topics
            topics.append(trend['name'])
            #storing counts of topics
            no_of_topics.append(trend['tweet_volume'])
    
    #creating pandas dataframe for concatinating the two list 
    top100 = pd.concat([pd.Series(topics),pd.Series(no_of_topics)],axis=1)\
                    .rename(columns={0:'||Trending_Topics||',1:'||No_of_tweets||'})\
                    .fillna(np.round(np.mean(top100['No of tweets'])))
    top100 = top100[:100]

    #saving it to txt file
    top100.to_csv('top100_India_trending_topics.txt', header=None, index=None, sep='\t', mode='a')
