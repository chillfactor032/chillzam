import os
import subprocess
import base64
import random
import platform
import argparse
import sys
import json
from shutil import which
from threading import Thread
import requests
import streamlink
from PySide6.QtCore import Signal, QObject

class ChillZam(Thread):

    class Signals(QObject):
        status_update = Signal(str, int)
        result = Signal(dict)

    def __init__(self, twitch_channel, twitch_gql_token, shazam_api_key, working_dir, ffmpeg_path):
        Thread.__init__(self)
        self.twitch_channel = twitch_channel
        self.twitch_gql_token = twitch_gql_token
        self.shazam_api_key = shazam_api_key
        self.working_dir = working_dir
        self.twitch_url = f"https://twitch.tv/{twitch_channel}"
        self.ffmpeg_path = ffmpeg_path
        self.signals = ChillZam.Signals()
        self.output = {
            "artist": "",
            "song": "",
            "album_art": "",
            "error": "",
            "remaining": -1
        }

    def twitch_gql_token_valid(self):
        url = "https://gql.twitch.tv/gql"
        headers = {
            "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
            "Content-Type": "text/plain",
            "Authorization": f"OAuth {self.twitch_gql_token}"
        }
        data = [
            {
                "operationName": "SyncedSettingsEmoteAnimations",
                    "variables": {},
                    "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "64ac5d385b316fd889f8c46942a7c7463a1429452ef20ffc5d0cd23fcc4ecf30"
                    }
                }
            }
        ]
        response = requests.post(url, headers=headers, json=data, timeout=10)
        return response.status_code == 200

    #Song Data is Base64 Encoded
    def detect_song(self, raw_audio_b64, api_key):
        requests_left = -1
        url = "https://shazam.p.rapidapi.com/songs/v2/detect"
        querystring = {"timezone":"America/Chicago","locale":"en-US"}
        headers = {
            "content-type": "text/plain",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "shazam.p.rapidapi.com"
        }
        response = requests.post(url, data=raw_audio_b64, headers=headers, params=querystring, timeout=15)
        if "x-ratelimit-requests-remaining" in response.headers:
            requests_left = response.headers["x-ratelimit-requests-remaining"]
        return requests_left, response.json()

    def convert_to_raw_audio(self, ffmpeg, in_file, out_file):
        proc = subprocess.run([ffmpeg, '-i', in_file, "-vn", "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", "-f", "s16le", out_file], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, check=False, shell=True)
        return proc.returncode == 0

    def record_stream(self, outfile, max_bytes=200):
        session = streamlink.Streamlink()
        session.set_plugin_option("twitch", "api-header", [("Authorization", f"OAuth {self.twitch_gql_token}")])
        streams = session.streams(self.twitch_url)
        if len(streams) == 0 or "worst" not in streams.keys():
            self.output["error"] = "Stream is not available"
            return False
        stream_obj = streams["worst"]
        fd = stream_obj.open()
        chunk = 1024
        num_bytes = 0
        data = b''
        while num_bytes <= max_bytes*1024:
            data += fd.read(chunk)
            num_bytes+=chunk
        fd.close()
        with open(outfile, "wb") as file:
            file.write(data)
        return os.path.exists(outfile) 
    
    def run(self):
        #Test validity of GQL OAuth token
        if not self.twitch_gql_token_valid():
            self.output["error"] = "Twitch GQL Token Expired"
            self.result()
            return

        # record stream audio
        random_file_name = str(random.randint(10000000,99999999))
        stream_recording_file = os.path.join(self.working_dir, f"{random_file_name}.acc")
        raw_recording_file = os.path.join(self.working_dir, f"{random_file_name}.raw")
        if not self.record_stream(stream_recording_file):
            self.result()
            return
        
        # Convert Stream Audio into Raw Format for Shazam
        if not self.convert_to_raw_audio(self.ffmpeg_path, stream_recording_file, raw_recording_file):
            self.output["error"] = "Error converting stream audio from ACC to raw PCM s16le"
            self.result()
            return

        #Encode raw audio to base64
        with open(raw_recording_file, "rb") as song:
            songBytes = song.read()
            songb64 = base64.b64encode(songBytes)
            l = len(songb64)
            #Detect the song
            try:
                requests_remaining, matches = self.detect_song(songb64, self.shazam_api_key)
            except requests.exceptions.ReadTimeout as exception:
                self.output["error"] = "Request to Shazam timed out. Try again."
                self.result()
                return
            
            self.output["remaining"] = requests_remaining

            if "track" in matches.keys():
                if "title" in matches["track"].keys():
                    self.output["song"] = matches["track"]["title"]
                if "subtitle" in matches["track"].keys():
                    self.output["artist"] = matches["track"]["subtitle"]
                if "images" in matches["track"].keys() and "coverart" in matches["track"]["images"].keys():
                    self.output["album_art"] = matches["track"]["images"]["coverart"]
            else:
                self.output["error"] = "Song not identified"

        #Remove the temp files
        if os.path.exists(stream_recording_file):
            os.remove(stream_recording_file)
        if os.path.exists(raw_recording_file):
            os.remove(raw_recording_file)

        # Return the result
        self.result()

    def status(self, msg, timeout=5):
        self.signals.status_update.emit(msg, timeout)

    def result(self):
        print(self.output)
        self.signals.result.emit(self.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use the Shazam API to detect the current playing song on a Twitch stream.")
    parser.add_argument("-c", "--config", help="Path to config file. Check the README for an example")
    parser.add_argument("-v", "--verbose", action="store_true", help="Path to ffmpeg - used for converting audio.")
    args = parser.parse_args()

    out = {
        "artist": "",
        "song": "",
        "album_art": "",
        "error": "",
        "remaining": -1
    }
    
    """Find the config file"""
    config_path = ""
    if args.config:
        if os.path.exists(args.config):
            config_path = args.config
        else:
            out["error"] = "Specified config file does not exist."
            print(out)
            sys.exit(1)
    else:
        if not os.path.exists(config_path):
            out["error"] = "No config file could be found. Specify with -c option or a config.json in script dir."
            print(out)
            sys.exit(1)

    try:
        with open(config_path) as config_file:
            config = json.load(config_file)
    except Exception as e:
        out["error"] = "Could not load json config file. Improper json formatting?"
        print(out)
        sys.exit(1)

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
    system = platform.system()
    if not ffmpeg_path:
        ffmpeg_source = "Provided by repository"
        if system == "Windows":
            ffmpeg_path = os.path.join(script_dir, "bin", "win", "ffmpeg-win64.exe")
        elif system == "Linux":
            out["error"] = "FFmpeg is not installed. Install it using your package manager."
            quit(out, 1)
        elif system == "Darwin":
            ffmpeg_path = os.path.join(script_dir, "bin", "mac", "ffmpeg")
        else:
            out["error"] = f"Unsupported OS Detected: {system}"
            print(out)
            sys.exit(1)

    """Confirm FFmpeg exists based on path"""
    if not os.path.exists(ffmpeg_path):
        out["error"] = f"Could not find FFmpeg. Confirm it exists at path: {ffmpeg_path}"
        print(out)
        sys.exit(1)

    working_dir = ""
    if "working_dir" in config.keys():
        working_dir = config["working_dir"]
        if working_dir is not None or working_dir != "":
            if not os.path.exists(working_dir):
                working_dir = ""

    cz = ChillZam(config['twitch_channel'], 
                config["twitch_gql_oauth_token"], 
                config["shazam_api_key"], 
                working_dir, 
                ffmpeg_path)
    cz.start()
    cz.join()