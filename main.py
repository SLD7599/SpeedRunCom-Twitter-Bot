import urllib2
import json
from speedrundata import SpeedrunData
import tweepy
import time
from constants import *

class Speedrun(SpeedrunData):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    def __init__(self, pos):
        self.pos = pos

        self.time = SpeedrunData.getTime(self, pos)
        self.user = SpeedrunData.findPlayer(self, pos)
        self.category = SpeedrunData.getCategory(self, pos)
        self.video = SpeedrunData.getVideo(self, pos)
        self.twitter = SpeedrunData.checkTwitter(self, pos)

    #Forms tweet from data
    def formTweet(self):
        if self.twitter == None:
            if self.video == None:
                tweet = "Congratulations to %s on getting a %s in %s %s!" % (self.user, self.time, GAME_NAME, self.category)
            else:
                tweet = "%s %s in %s by %s: %s" % (GAME_NAME, self.category, self.time, self.user, self.video)
        else:
            if self.video == None:
                tweet = "Congratulations to %s on getting a %s in %s %s!" % (self.twitter, self.time, GAME_NAME, self.category)
            else:
                tweet = "%s %s in %s by %s: %s" % (GAME_NAME, self.category, self.time, self.twitter, self.video)
        return tweet

    def checkTweet(self):
        usertweets = self.api.user_timeline(count=50, include_rts=False)
        stats = []

        tweet_present = True
        for status in usertweets:
            stats.append(status.text)
        if self.formTweet in stats:
            tweet_present = False
        return tweet_present


    def sendTweet(self):
        if self.checkTweet() == True:
            self.api.update_status(status=self.formTweet())
        time.sleep(3600)

if __name__ = "__main__":
    while True:
        latestrun = Speedrun(0)
        latestrun.sendTweet()
