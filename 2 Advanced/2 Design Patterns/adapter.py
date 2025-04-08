"""
The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces
to work together. It acts like a bridge between two interfaces.

Intent: To convert the interface of a class into another interface the client expects.

"""


# Target Interface
class AudioPlayer:
    def play_audio(self, filename: str):
        raise NotImplementedError


# Adaptee
class VideoPlayer:
    def __init__(self, codec: str):
        self.codec = codec

    def play_video(self, filename: str):
        print(f"Playing video '{filename}' with codec '{self.codec}'")


# Adapter
class VideoToAudioAdapter(AudioPlayer):
    def __init__(self, video_player: VideoPlayer):
        self.video_player = video_player

    def play_audio(self, filename: str):
        print(f"[Adapter] Extracting audio from video...")
        self.video_player.play_video(filename)
        print(f"[Adapter] Simulating audio playback of '{filename}'\n")

    @property
    def codec(self):
        return self.video_player.codec


# Client Code
def start_audio(player: AudioPlayer, filename: str):
    print(f"Now playing: {filename}")
    player.play_audio(filename)


# Usage
video = VideoPlayer(codec="H.264")
adapter = VideoToAudioAdapter(video)

print(f"Using video codec: {adapter.codec}")
start_audio(adapter, "movie_trailer.mp4")
