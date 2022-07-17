from pytube import Playlist

playlist = Playlist('https://youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9')
for video in playlist.videos:
    video.streams.first().download()
