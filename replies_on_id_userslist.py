# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:25:03 2019

@author: Ghayasuddin Adam
"""


import tweepy
from tweepy import OAuthHandler

#insert Twitter Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

alltweets = []
def getTweet(screen_name):
    alltweets.clear()	
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode="extended")
    alltweets.extend(new_tweets)
	
    oldest = alltweets[-1].id - 1
	
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode="extended")
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1


replies_id=[]
replied = []
name=['BarcaWorldwide', 'Zuby2510', 'GhayasAdam']
id_parse = ['1195425989540663303']
count=0
id_count = len(id_parse)
name_count = len(name)
name_ind = 0
id_ind = 0

 

while id_count > 0:
    while name_count > 0:
        getTweet(name[name_ind])
        for tweet in alltweets:
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                    if (tweet.in_reply_to_status_id_str==id_parse[id_ind]):
                        print(tweet.full_text)
                        id_parse.append(tweet.id_str)
                        id_count += 1
                        count += 1
                        replied.append(name[name_ind])
        name_ind += 1
        name_count -= 1
    id_ind += 1
    id_count -= 1
    name_ind = 0
    name_count = len(name)


print("Replies Count: ")
print(count)
print("Repliers screen_names: ")
print(replied)