# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:09:38 2019

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

screen_name = "BarcaWorldwide"

allfav = []	
uss = api.favorites(screen_name = screen_name,count=200)
allfav.extend(uss)
oldest = allfav[-1].id - 1

while len(uss) > 0:
    print ("getting favourites before %s" % (oldest))
		
    uss = api.favorites(screen_name = screen_name,count=200,max_id=oldest)
		
    allfav.extend(uss)

    oldest = allfav[-1].id - 1


fav = set()
for i in range(0, len(allfav)):
    fav.add(allfav[i].user.screen_name)
    
print(fav)
