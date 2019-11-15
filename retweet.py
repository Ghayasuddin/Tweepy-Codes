# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:14:55 2019

@author: Ghayasuddin Adam
"""

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

#insert Twitter Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)

screen_name = 'GhayasAdam'

alltweets = []	
new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode="extended")
alltweets.extend(new_tweets)
	
oldest = alltweets[-1].id - 1
i = 0
while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode="extended")
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1


import time

auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)   

print("Who retweeted me")
retweeted_me = set()
for i in range(0,len(alltweets)):
    if alltweets[i].retweeted is False:
        try:
            pp = api.retweets(alltweets[i].id)
            for j in range(0,len(pp)):
                retweeted_me.add(pp[j].user.screen_name)
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue       

print(retweeted_me)

print("Who i retweeted")
i_retweeted = set()
for i in range(0,len(alltweets)):
    if alltweets[i].retweeted is True:
        try:
            i_retweeted.add(alltweets[i].retweeted_status.user.screen_name)
        except:
            continue       

print(i_retweeted)