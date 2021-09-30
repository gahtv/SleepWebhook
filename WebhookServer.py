# import stuff i need
import tweepy
import random
import json
from flask import Flask, request
from discord import Webhook, AsyncWebhookAdapter  # using pycord instead of discord.py
import aiohttp
import asyncio
import subprocess
# json dumb stuff
oauth = json.load(open("twitter.json"))
DiscordTokens = json.load(open("discord.json"))
url = DiscordTokens["url"]
ping = DiscordTokens["ping"]
consumer_key = oauth["consumer"]
consumer_secret = oauth["consumer_secret"]
access_token = oauth["access"]
access_secret = oauth["access_secret"]
# discord dumb stuff


async def send(sent):
    async with aiohttp.ClientSession() as session:
        webhooks = Webhook.from_url(url=url, adapter=AsyncWebhookAdapter(session=session))
        await webhooks.send(" {} https://twitter.com/{}/status/{}".format(ping, username, sent.id))
choices = [1, 2, 3]  # just to make sure tweets are different
# tweepy dumb stuff
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
username = api.verify_credentials().screen_name
app = Flask(__name__)  # ooh server
alarm = "d:\\path\\to\\file"  # cool alarm


async def play():
    subprocess.Popen("vlc " + alarm + " vlc:quit")


async def stop():
    subprocess.Popen("TASKKILL /IM VLC.EXE")


@app.route('/webhook', methods=['POST'])  # fancy cool flask very cool
async def webhook():
    choice = 1
    # more prns stuff;
    prns = random.choice(["he", "she", "they"])
    aprns = random.choice(["he's", "she's", "they're"])
    sleepwebhook = request.json
    print(sleepwebhook)
    if "sleep_tracking_started" == sleepwebhook.get("event"):  # night nerd
        tweet = api.update_status("yeah gahtv is sleeping")
        asyncio.run(send(sent=tweet))
        api.update_profile(description="i am sleeping")
        print("sweet dreams")
    elif "alarm_alert_start" == sleepwebhook.get("event"):  # wake up
        choice = random.choice(choices)
        api.update_profile(description="i should be awake")
        if choice == 1:
            tweet = api.update_status("morning gahtv, or maybe {} just forgot to mute the other alarms, whatever".format(prns))  # yeah dumbass
        elif choice == 2:
            tweet = api.update_status("rise and shine dip shit, you should be awake, or you just keep forgetting to mute other alarms, in that case screw you")  # screw them right
        elif choice == 3:
            tweet = api.update_status("Hey, gahtv. You should be finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.")  # haha funny vidya game reference
        else:
            tweet = api.update_status("rise and shine dip shit, you should be awake, or you just keep forgetting to mute other alarms, in that case screw you")
        asyncio.run(send(sent=tweet))
        print("Opening VLC...")
        asyncio.run(play())
    elif "alarm_alert_dismiss" == sleepwebhook.get("event"):  # thank you for waking up
        choice = random.choice(choices)
        api.update_profile(description="i am awake")
        if choice == 1:
            tweet = api.update_status("oh {} just finally woke up, or maybe AGAIN {} just forgot to mute the other alarms, whatever".format(prns, prns))  # thank you
        elif choice == 2:
            tweet = api.update_status("thanks for finally waking up, puts a lot less strain on me, the computer, unless you dont mute the alarms, in that case fuck you")  # so true
        else:
            tweet = api.update_status("thanks for dismissing that alarm, make sure to dismiss the others in advance")  # so true
        asyncio.run(send(sent=tweet))
        print("Killing VLC...")
        asyncio.run(play())
    elif "time_to_bed_alarm_alert" == sleepwebhook.get("event"):  # please sleep
        choice = random.choice(choices)
        api.update_profile(description="i should be sleeping")
        if choice == 1:
            tweet = api.update_status("holy hell {} should be sleeping like rn so idk wtf {} doing but whatevs".format(prns, aprns))  # they should be am i right
        elif choice == 2:
            tweet = api.update_status("please sleep like rn gahtv, sleep like rn, don't go on tiktok and forget me ok")  # they probs went on tiktok am i right
        else:
            tweet = api.update_status(r"hey {} should be sleeping like now, maybe {} is rn tho and just forgor 💀 and didnt press sleep tracking".format(prns, prns))  # they did
        asyncio.run(send(sent=tweet))
    print(str(choice))
    return 'success', 200


if __name__ == '__main__':
    app.run(host="192.168.2.143", port=5000)