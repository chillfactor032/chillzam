import argparse
import os
import platform
import sys
import json
import streamlink
import requests
import subprocess
import base64
from shutil import which

system = platform.system()
script_dir = os.path.realpath(os.path.dirname(__file__))
config_path = os.path.join(script_dir, "config.json")
config_src = "config.json in script dir"
config = {}

parser = argparse.ArgumentParser(description="Use the Shazam API to detect the current playing song on a Twitch stream.")
parser.add_argument("-c", "--config", help="Path to config file. Check the README for an example")
parser.add_argument("-v", "--verbose", action="store_true", help="Path to ffmpeg - used for converting audio.")
args = parser.parse_args()

def verbose_log(msg):
    if args is not None and args.verbose:
        print(msg)

verbose_log("=== ChillZam! ===")
verbose_log(f"Detected Platform: {system}")
verbose_log(f"Script Dir: {script_dir}")
verbose_log(f"Args: {args}")

"""Find the config file"""
if args.config:
    if os.path.exists(args.config):
        config_path = args.config
        config_src = "CLI arg"
    else:
        sys.stderr.write("Specified config file does not exist.")
        sys.exit(1)
else:
    if not os.path.exists(config_path):
        sys.stderr.write("No config file could be found. Specify with -c option or a config.json in script dir.")
        sys.exit(1)

try:
    with open(config_path) as config_file:
        config = json.load(config_file)
        verbose_log("Config file loaded.")
except Exception as e:
    sys.stderr.write("Could not load json config file. Improper json formatting?")
    sys.exit(1)

verbose_log(f"Config File: {config_path}")
verbose_log(f"Config File Source: {config_src}")

""" 
If ffmpeg path is not specified in config,
see if there is ffmpeg in PATH
"""
ffmpeg_source = "Config File"
ffmpeg_path = config["ffmpeg_path"]
if not os.path.exists(ffmpeg_path):
    ffmpeg_path = which("ffmpeg")
    if ffmpeg_path:
        ffmpeg_source = "PATH"

"""
If ffmpeg not in PATH or specified
use a versions from the
repository (Windows or Mac)
if linux - use package manager to install first
"""
if not ffmpeg_path:
    ffmpeg_source = "Provided by repository"
    if system == "Windows":
        ffmpeg_path = os.path.join(script_dir, "bin", "win", "ffmpeg-win64.exe")
    elif system == "Linux":
        print("FFmpeg is not installed. Install it using your package manager.")
        sys.exit(1)
    elif system == "Darwin":
        ffmpeg_path = os.path.join(script_dir, "bin", "mac", "ffmpeg")
    else:
        print(f"Unsupported OS Detected: {system}")
        sys.exit(1)

verbose_log(f"FFmpeg Source: {ffmpeg_source}")
verbose_log(f"FFmpeg Path: {ffmpeg_path}")

"""Confirm FFmpeg exists based on path"""
if not os.path.exists(ffmpeg_path):
    print("Could not find FFmpeg. Confirm it exists at path:")
    print(ffmpeg_path)
    sys.exit(1)
else:
    verbose_log("Confirmed FFmpeg exists.")

#Song Data is Base64 Encoded
def detectSong(raw_audio_b64, api_key):
    url = "https://shazam.p.rapidapi.com/songs/v2/detect"
    querystring = {"timezone":"America/Chicago","locale":"en-US"}
    headers = {
        "content-type": "text/plain",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }
    response = requests.post(url, data=raw_audio_b64, headers=headers, params=querystring)
    return response.json()

def convert_to_raw_audio(ffmpeg, in_file, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)
    if args.verbose:
        subprocess.run([ffmpeg, '-i', in_file, "-vn", "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", "-f", "s16le", out_file])
    else:
        subprocess.run([ffmpeg, '-i', in_file, "-vn", "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", "-f", "s16le", out_file], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
    return os.path.exists(out_file)

def record_stream(url, out_file, oauth_token, max_bytes=200):
    #Remove out_file if it exists
    if os.path.exists(out_file):
        os.remove(out_file)
    session = streamlink.Streamlink()
    session.set_plugin_option("twitch", "api-header", [("Authorization", f"OAuth {oauth_token}")])
    streams = session.streams(url)
    stream_obj = streams["worst"]
    verbose_log(f"Stream: {stream_obj}")
    fd = stream_obj.open()
    chunk = 1024
    num_bytes = 0
    data = b''
    while num_bytes <= max_bytes*1024:
        data += fd.read(chunk)
        num_bytes+=chunk
    fd.close()
    with open(out_file, "wb") as file:
        file.write(data)
    return os.path.exists(out_file)

""" Script Logic """
verbose_log(f"Twitch URL: {config['twitch_channel']}")
verbose_log(f"Begin recording stream ({config['kbytes_to_record']} bytes)")
stream_audio_file = "output.acc"
if record_stream(config["twitch_channel"], stream_audio_file, config["twitch_gql_oauth_token"], config["kbytes_to_record"]):
    verbose_log("Stream audio recorded successfully")
else:
    sys.stderr.write("Error recording stream audio.")
    sys.exit(1)
raw_audio_file = "output.raw"
if convert_to_raw_audio(ffmpeg_path, stream_audio_file, raw_audio_file):
    verbose_log("Audio converted successfully")
else:
    sys.stderr.write("Error converting stream audio from ACC to raw PCM s16le")
    sys.exit(1)

#Encode raw audio to base64
with open(raw_audio_file, "rb") as song:
    songBytes = song.read()
    songb64 = base64.b64encode(songBytes)
    l = len(songb64)
    #Detect the song
    matches = detectSong(songb64,config["shazam_api_key"])
    if matches["track"]:
        title = matches["track"]["title"]
        artist = matches["track"]["subtitle"]
        print(f"Song Detected: {title} by {artist}")
        sys.exit(0)
    else:
        print("Could not detect song.")
        sys.exit(0)
