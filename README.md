# SleepWebhook
**A Python/Flask Server that interacts with [Sleep As Android](https://play.google.com/store/apps/details?id=com.urbandroid.sleep)**
## How It Works
When events happen on the Sleep As Android, it POST requests a JSON file to the server running this app, then when certain events happen, it will tweet and will post the url to a Discord channel, and when an alarm rings, it will ring an audio file via VLC
## Dependencies 
Tweepy, PyCord, Flask, VLC
## Operating Systems
Currently only on Windows, however I am working on getting it on Ubuntu/Other Linux Distros.
## Example
Currently, I am running an instance with this [Twitter Account](https://twitter.com/gahtvsleepsched "gahtv's sleep schedule").
