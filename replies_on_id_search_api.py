# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:54:58 2019

@author: Ghayasuddin Adam


If you are using free search api then it only has access to 7 days old data so you might get nothing on older tweets
But using this method you can make a better reply network
"""

import tweepy
from tweepy import OAuthHandler

#insert Twitter Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


screen_name = 'BarcaWorldwide'
id_str = '1195425989540663303'  

replies_id=[]
name=[]
id_parse = []
count=0
replies = 1
            
name.append(screen_name)
id_parse.append(id_str)
name_ind = 0
while replies > 0:
    for tweet in tweepy.Cursor(api.search,q='to:'+name[name_ind],result_type='recent',timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==id_parse[name_ind]):
                print(tweet.text)
                count += 1
                name.append(tweet.user.screen_name)
                replies += 1
                id_parse.append(tweet.id_str)
                replies_id.append(tweet)
    replies -= 1
    name_ind += 1
    flag = 0

print("Replies Count: ")
print(count)
print("Repliers screen_names: ")
print(name)