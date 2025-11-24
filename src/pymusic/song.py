from pydub import AudioSegment
from enum import Enum
from dataclasses import dataclass
import ffmpeg
import os
import json
from pathlib import Path

class SongExtension(Enum):
    mp3 = 1
    wav = 2

@dataclass
class Metadata:
    file_path: str
    title: str
    length: float
    date: int
    extension: SongExtension

def create_audio_segment(path_to_song: str, ext: str) -> AudioSegment:
    return AudioSegment.from_file(path_to_song, ext) 

class Song:
    def __get_song_metadata(self, path_to_song: str):
        path_info = Path(path_to_song)
        file_name: str = path_info.name 
        extension: str = path_info.suffix 

        print(file_name, extension)

        info = ffmpeg.probe(path_to_song)
        info_as_json: dict = json.loads(info)

        info_keys = info_as_json.keys()
        print(info_keys)     

    def __init__(self, path_to_song: str):
        self.metadata: Metadata = self.__get_song_metadata(path_to_song)
        # self.audio_segment: AudioSegment = __create_audio_segment(p)
        
    

