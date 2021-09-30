from discord.ext import commands
import discord
import json
import asyncio
import tweepy
import random

oauth = json.load(open("twitter.json"))
discordtoken = json.load(open("discord.json"))["bot_token"]
consumer_key = oauth["consumer"]
consumer_secret = oauth["consumer_secret"]
access_token = oauth["access"]
access_secret = oauth["access_secret"]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
bot = commands.Bot(command_prefix="slepr ")

client = discord.Client()


@bot.command()
async def status(ctx):
    a = api.verify_credentials().description
    game = discord.Game(str(a))
    print(str(a))
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.send(a)
    await asyncio.sleep(120)
    await bot.change_presence(status=discord.Status.idle)


@bot.command()
async def latest(ctx):
    a = api.user_timeline(screen_name="gahtvsleepsched")[0]
    print(str(a.text[0:30]))
    game = discord.Game("LATEST TWEET: "+str(a.text))
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.send("https://twitter.com/{}/status/{}".format(a.user.screen_name, a.id))
    await asyncio.sleep(120)
    await bot.change_presence(status=discord.Status.idle)


if __name__ == '__main__':
    bot.run(discordtoken)
    asyncio.sleep(5)
