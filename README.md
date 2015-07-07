# SpeedRunCom-Twitter-Bot
A Twitter bot that tweets out new speedruns using the [Speedrun.com API](https://github.com/speedruncom/api).

## How to use:
I tried to make this guide as user friendly as possible. If you still have questions email me at mikemallon99@gmail.com.

Things that you need to have installed:
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Tweepy](https://github.com/tweepy/tweepy)

Next, you want to create a new [Twitter App](https://apps.twitter.com/). You can name it anything that you want.
Then, open your app and click on the "Keys and Access Tokens" tab. They already give you the consumer key and secret,
you just need to generate new Access Tokens.

Once you have all of your keys, open constants.py and put your keys into the corresponding variables.
You also want to insert your game's ID, which can be found by going to your game's page on [speedrun.com](http://www.speedrun.com) and click "Access as JSON".
Just copy the string of letters under "id" and paste them into the GAME_ID variable. Lastly, put the name of you game under
the GAME_NAME variable.

To run the bot, open up the terminal in the SpeedRunCom-Twitter-Bot folder and type "python main.py". You need to keep
the terminal open running this at all times or else the bot wont work.

**Note**: If you want your bot to work for multiple different games, you need to run multiple instances of the bot set to different games. If I can find a way to get runs from a game series, I'll be sure to implement it.

**P.S.: This is my first real project, so the code isn't as optimized as it could be.**
  
