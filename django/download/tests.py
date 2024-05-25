from time import sleep
import json
import os
import playsound
def playNextSong():
    songDir = "E:/Coding/Github/RaspberryPiSongRequest/django/temp/"
    playlistPath = "E:/Coding/Github/RaspberryPiSongRequest/django/playlist.json"
    with open(playlistPath, "r") as f:
        playlist = json.load(f)
        print(playlist["query"])
        query = playlist["query"]
    now = query.pop(0)
    print(now)
    print(os.path.join(songDir,now))
    playsound(os.path.join(songDir,now))
    print(now + " is done playing")

while True:
    playNextSong()
  
