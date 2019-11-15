# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:46:39 2019

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

api = tweepy.API(auth)

import urllib
import re

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib.request.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        json_data = json_data.decode('utf-8')
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids

    except urllib.request.HTTPError:
        return False


screen_name = 'GhayasAdam'

alltweets = []	
new_tweets = api.user_timeline(screen_name = screen_name,count=200)
alltweets.extend(new_tweets)
	
oldest = alltweets[-1].id - 1
	
while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1

ids = []
for i in range(0,len(alltweets)):
    if alltweets[i].favorite_count > 0 and alltweets[i].retweeted is False:
        ids.extend(get_user_ids_of_post_likes(alltweets[i].id))

uniqueids = set(ids)

for i in uniqueids:
    user = api.get_user(i)
    print (user.screen_name)
