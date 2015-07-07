import urllib2
import json
from constants import *

class SpeedrunData:
    main = "http://www.speedrun.com/api/v1/runs?game=%s&orderby=verify-date&direction=desc" % GAME_ID
    openmain = urllib2.urlopen(main)
    mainjson = json.load(openmain)

    #Checks if the user has a Twitter
    def checkTwitter(self, pos):
        user_twitter = None
        try:
            playerid = self.mainjson["data"][pos]["players"][0]["id"]
            openplayer = json.load(urllib2.urlopen("http://www.speedrun.com/api/v1/users/%s" % playerid))

            user_twitter = openplayer["data"]["twitter"]["uri"]
            user_twitter = user_twitter.replace("http://www.twitter.com/", "@")
            if "%40" in user_twitter or "%20" in user_twitter:
                user_twitter = user_twitter.replace("%40", "")
                user_twitter = user_twitter.replace("%20", "")
        except:
            pass
        return user_twitter

    #Retrieves Player Username
    def findPlayer(self, pos):
        try:
            username = self.mainjson["data"][pos]["players"][0]["name"]
        except:
            playerid = self.mainjson["data"][pos]["players"][0]["id"]
            openplayer = json.load(urllib2.urlopen("http://www.speedrun.com/api/v1/users/%s"% playerid))
            username = openplayer["data"]["names"]["international"]
        return username

    #Takes Input Time and Outputs Proper Format
    def prettyTime(self, time):
        time = time.strip('PT')
        time = time.strip("S")
        time = time.replace("H", ":")
        time = time.replace("M", ":")

        split_time = time.split(":")
        if len(split_time) == 3:
            if len(split_time[1]) == 1:
                split_time[1] = "0" + split_time[1]
            if len(split_time[2]) == 1:
                split_time[2] = "0" + split_time[2]
        if len(split_time) == 2:
            if len(split_time[1]) == 1:
                split_time[1] = "0" + split_time[1]

        colon = ":"
        time = colon.join(split_time)

        return time

    #Retrieves Time
    def getTime(self, pos):
        time = self.mainjson["data"][pos]["times"]["realtime"]
        time = self.prettyTime(time)
        return time

    #Retrieves Category Name
    def getCategory(self, pos):
        categoryid = self.mainjson["data"][pos]["category"]
        opencategory = json.load(urllib2.urlopen("http://www.speedrun.com/api/v1/categories/%s" % categoryid))
        categoryname = opencategory["data"]["name"]
        return categoryname


    def getDate(self, pos):
        rawdate = self.mainjson["data"][pos]["submitted"]
        return rawdate

    #Gets video url, twitch.tv link is top priority
    def getVideo(self, pos):
        try:
            videos = self.mainjson["data"][pos]["videos"]["links"]
            videourl = None

            for link in videos:
                if "twitch.tv" in link["uri"]:
                    videourl = link["uri"]
                    return videourl
            if videourl == None:
                videourl = videos[0]["uri"]
            return videourl
        except:
            return None

