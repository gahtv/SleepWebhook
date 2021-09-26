# SleepWebhook
**A Python/Flask Server that interacts with [Sleep As Android](https://play.google.com/store/apps/details?id=com.urbandroid.sleep)**
## How It Works
When [events](https://docs.sleep.urbandroid.org/services/automation.html#events) happen on the Sleep As Android app, it POST requests a JSON file to the server running this app, then when certain events happen, it will tweet and will post the url to a Discord channel, and when an alarm rings, it will play an audio file via VLC.
|Event|What Happens|
|-----|------------|
|Start Sleep Tracking|Tweets out you are sleeping, changes profile description, and sends out link to tweet in Discord channel|
|Alarm Rings|Tweets out you should wake up, changes profile description, starts up VLC with the audio file of your choice, and sends out link to tweet in Discord channel|
|Alarm Dismisses|Tweets out you are awake, changes profile description, kills VLC, and sends out link to tweet in Discord channel|
|Time To Bed|Tweets out you should sleep, changes profile description, and sends out link to tweet in Discord channel|
|Future?|If you want to see something added, start a pull request.|
## Dependencies - also in requirements.txt
```
tweepy==4.0.0
Flask==1.1.4
requests==2.26.0
PyCord==1.7.3
Python==3.9
```
## Operating Systems
Currently only on Windows, however I am working on getting it on Ubuntu/Other Linux Distros.
## Example
Currently, I am running an instance with this [Twitter Account](https://twitter.com/gahtvsleepsched "gahtv's sleep schedule").
## Run It Yourself
Download the source code, and change the `discord.json` and the `tweet.json` files to your own tokens/url/ping, generated via Twitter's [developer portal](https://developer.twitter.com), and a Discord channel webhook. Change the file path to what file you want playing when the alarm rings in `WebhookServer.py`. If you want to, change the pronouns you want to use in `WebhookServer.py`. Run the python script, and you should be up and running!
