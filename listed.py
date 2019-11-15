# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:26:28 2019

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

screen_name = 'HakJags'

uss = api.lists_memberships(screen_name)

print("People Who Has listed me")
us = []
for i in range(0,len(uss)):
    us.append(uss[i].user.screen_name)


print(us)

uss = api.lists_all(screen_name)
print("People Whom I listed")
we = []
for i in range(0,len(uss)):
    if(uss[i].user.screen_name == screen_name):
        mem = api.list_members(screen_name, uss[i].name)
        for j in range(0, len(mem)):
            we.append(mem[j].screen_name)

print(we)