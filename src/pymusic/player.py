from pydub import AudioSegment
from pydub.playback import play
from queue import SimpleQueue
from pymusic.song import Song

class Player:
    def __init__(self):
        self.__queue: SimpleQueue[Song] = SimpleQueue()
        self.current_song: Song | None = None

    def play_next(self):
        if self.__queue.empty() is not True:
            self.current_song = self.__queue.get() 
            
            
            play(self.current_song)

