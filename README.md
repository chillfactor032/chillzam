# ChillZam!
 Use the Shazam API to detect the song currently playing on a Twitch stream.

 This tool uses [Streamlink](https://streamlink.github.io/) to record a few seconds of a specified Twitch stream, then it converts the audio to the format required by the [Shazam API](https://rapidapi.com/apidojo/api/shazam).

 You will need to find out your Twitch GQL OAuth token. This token is different from the traditional Helix Twitch API token. If you need help finding the token check out this issue from the Streamlink github:
 
  [How do I get a Twitch OAuth token to authenticate my requests?](https://github.com/streamlink/streamlink/discussions/4400)


You will also need to generate a Shazam API key as well. Shazam has a free tier that allows 500 requests per month. Head over to the [Shazam Rapid API](https://rapidapi.com/apidojo/api/shazam) page and subscribe to it. You will automatically get a key.

ChillZam uses FFmpeg to convert the audio to the Shazam format. If you have FFmpeg on your system already, just specify the path to it in the config file. If a path is not specified it will look in your PATH to see if its there. If its not in the config OR the PATH, it will attempt to use the binary in the `/bin` directory. This works for Windows and Mac. If you are on a Linux system you will need to install FFmpeg using your package manager.

The script needs a config file to operate. This config file can be specified at the command link or just include a config.json file adjacent to the script. The config file has the following format:

```json
{
    "twitch_channel": "https://www.twitch.tv/somestreamer",
    "twitch_gql_oauth_token": "xxxxxxxxxxxxxxxxxxxxxxx",
    "shazam_api_key": "xxxxxxxxxxxxxxxxxxxxxxx",
    "ffmpeg_path": "",
    "working_dir": "",
    "kbytes_to_record": 200,
    "show_requests_remaining", true
}
```

The only field not mentioned yet is `kbytes_to_record`. 200KB is a good starting point. If its not identifying any songs, try to bump that number up. The max size that Shazam supports is 500kb.

To use, clone the repository and run pip install on the requirements.txt file.

```bash
git clone https://github.com/chillfactor032/chillzam.git
cd chillzam
py -m pip install -r requirements.txt
```

Be sure to create the config file, then run the script

```bash
py chillzam.py
```

For Mac or Linux you may need to use `python` or `python3` instead of `py`. 

# GUI Help [¶](#gui-help) 

If you wish to run this tool as a standalone GUI, an executable will be available in the release section. 

## Twitch Channel

This is simple the name of the Twitch channel you want ChillZam to listen to. If the url of the channel is "https://twitch.tv/shoud", then the channel name is simple "shroud".

## Getting a Twitch GPL Auth token

If you log into Twitch on your browser, you will have a Twitch GPL Auth Token in your cookies. How you view these is Browser dependent.

### Chrome

In Chrome, navigate to https://twitch.tv. When the page loads press F12 to bring up the DevTools. Navigate to the "Application" tab and then in the left bar select "Cookies" > "https://gpl,twitch.tv". The list of cookies for that domain will appear. Find the one named "auth-token" and double click it. Copy the value to your clipboard and paste it in the settings dialog in ChillZam!

### Firefox

In Firefox, navigate to https://twitch.tv. When the page loads press F12 to bring up the DevTools. Navigate to the "Storage" tab and then in the left bar select "Cookies" > "https://gpl,twitch.tv". The list of cookies for that domain will appear. Find the one named "auth-token" and double click it. Copy the value to your clipboard and paste it in the settings dialog in ChillZam!
Thanks!

## Shazam API Key

You will need to generate your own Shazam API Key. You will need to first create a RapidAPI account before you can subscribe to the API. Once you have an account created, navigate to "https://rapidapi.com/apidojo/api/shazam". Click the "Subscribe to Test" button. Select the "Basic" (Free) package which gets you 500 requests per month. You should see a message like "Subscription Created Successfully". Naviage back to "https://rapidapi.com/apidojo/api/shazam" and now you should see your API Key under a field called "X-RapidAPI-Key". Copy this value and paste it into the settings dialog in ChillZam!

### Donations

ChillZam is provided free and without warranty. If you feel compelled to donate here are my crypto addresses below.

**Coin** | **Address**
--- | ---
BTC | 3C7UT1a2Do3LxFvxZt88S7gsNkRyRKXYCw
ETH | 0xc24Fc5E6C2b3E1e1eaE62f59Fab8cFBC87b1FEfc
LTC | MViPMqjn2kdMwbLAbYtgpgnHfzwwpbzUZQ

### Contact

chill@chillaspect.com