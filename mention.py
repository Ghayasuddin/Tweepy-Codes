# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:37:10 2019

@author: Ghayasuddin Adam
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  3 07:41:43 2019

@author: Ghayasuddin Adam
"""
import re
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

api = tweepy.API(auth)

screen_name = 'BarcaWorldwide'

print("\nPeople Who Has mentioned me Search API")

allmention = []	

for tweet in tweepy.Cursor(api.search,q='@'+ screen_name,result_type='recent',timeout=999999).items(1000):
    if tweet.in_reply_to_status_id is None and tweet.retweeted is False and tweet.user.screen != screen_name:
        if len(tweet.entities["user_mentions"]) > 0:
            allmention.append(tweet)
    
mentions = set()
for i in range(0, len(allmention)):
    if allmention[i].in_reply_to_screen_name != screen_name:
        mentions.add(allmention[i].user.screen_name)
    
print(mentions)

print("\n People Who I Have mentioned")

alltweets = []	
new_tweets = api.user_timeline(screen_name = screen_name,count=200)
alltweets.extend(new_tweets)
	
oldest = alltweets[-1].id - 1
	
while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
        
mention = set()
for i in range(0,len(alltweets)):
    if alltweets[i].in_reply_to_status_id is None and alltweets[i].retweeted is False:
        if len(alltweets[i].entities["user_mentions"]) > 0:
            for j in range(0, len(alltweets[i].entities["user_mentions"])):
                mention.add(alltweets[i].entities["user_mentions"][j]["screen_name"])
        
print(mention)
