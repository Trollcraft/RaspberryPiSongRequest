from django.shortcuts import render
import os
from pytube import YouTube
from rpiclient import config
import json
import playsound
from time import sleep
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from moviepy.editor import AudioFileClip
# Create your views here.
def webmToWav(input_path, output_path):
    save_path = config["songpath"]
    audio_clip = AudioFileClip(os.path.join(save_path, input_path))
    audio_clip.write_audiofile(os.path.join(save_path, output_path))
    audio_clip.close()
    os.remove(os.path.join(save_path, input_path))
    return



@csrf_exempt
def playing(request):
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
        try:
            playNextSong()
        except:
            sleep(10)   

@csrf_exempt
def download(request):
    file_name = ""
    save_path = config["songpath"]
    songlistLink = os.path.join(save_path, "contents.json")
    with open(songlistLink, "r") as f:
        songlist = json.load(f)
    data = json.loads(request.body)
    link = data.get("link", "")
    print(link)
    print("checking if in database")
    if link in songlist:
        download = False
        output_wav = songlist[link]
        print("song in database")
    else:    
        print("song not in database")
        try:
            print("looking for song")
            song = YouTube(link)
            print("song found")
            audio_streams = song.streams.filter(only_audio=True).order_by('abr').desc()
            audio_stream = audio_streams.first()
            if not audio_stream:
                print("No suitable audio stream found")
                return HttpResponse({"message": "No suitable audio stream found"}, status=400)
            print("audio stream found \n Now downloading")
            audio_stream.download(output_path=save_path)
            print("download finished")
            file_name = audio_stream.default_filename
            print(f"File name set {file_name}")
            input_webm = file_name
            output_wav = file_name.replace(".webm", ".wav")
            webmToWav(input_webm, output_wav)
            download = True
            songlist[link] = output_wav
            print("song added to contents")
            with open(songlistLink,"w") as f:
                json.dump(songlist, f)
        except:
            print("error while download")
            return HttpResponse({"message" : "Error in Downloading"})
        
    playlistPath = "./playlist.json"
    with open(playlistPath, "r") as f:
        playlist = json.load(f)
        playlist["query"].append(output_wav)
    with open(playlistPath, "w") as f:
        json.dump(playlist, f)
    return HttpResponse({"download": download, "message": "Saved"})

def showPlaylist(request):
    playlistPath = "./playlist.json"
    with open(playlistPath, "r") as f:
        playlist = json.load(f)
        print(playlist["query"])
        query = playlist["query"]
    return JsonResponse({"query": query})