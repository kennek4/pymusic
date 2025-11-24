from pymusic.song import Song
import os

song_path: str = os.getcwd() + "/assets/Miniskirt.mp3"
print(song_path)

my_song = Song(song_path)
