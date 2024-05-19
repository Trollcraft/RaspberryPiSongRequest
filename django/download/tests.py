from time import sleep
import json
import pygame
import os
def playNextSong():
    songDir = "E:/Coding/Github/RaspberryPiSongRequest/django/temp/"
    playlistPath = "E:/Coding/Github/RaspberryPiSongRequest/django/playlist.json"
    with open(playlistPath, "r") as f:
        playlist = json.load(f)
        print(playlist["query"])
        query = playlist["query"]
    now = query.pop(0)
    pygame.mixer.init()
    print("Pygame mixer initialized")
    print(now)
    print(os.path.join(songDir,now))
    pygame.mixer.music.load(os.path.join(songDir,now))
    print("song loaded")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass

while True:
    playNextSong()
  
