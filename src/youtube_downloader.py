from pytube import YouTube
from pathlib import Path


class YouTubeDownloader:
    def __init__(self, output_path=None, quality=None):
        self.quality = quality
        
        if output_path == None:
            self.output_path = Path.cwd()
        else:
            self.output_path = output_path

    def download(self, url):
        self.url = url
        self.yt = YouTube(self.url)

        if self.quality == None:
            stream = self.yt.streams.filter(
                progressive=True, file_extension="mp4"
                ).get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True, file_extension="mp4", res=self.quality
                ).first() 

        stream.download(self.output_path)

if __name__ == "__main__":
    kurt = YouTubeDownloader()
    kurt.download("https://youtu.be/R3XIGon2RjY?si=22QWptuuyRsPfLeW")
