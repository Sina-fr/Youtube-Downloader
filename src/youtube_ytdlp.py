from yt_dlp import YoutubeDL
from pathlib import Path


class YutubeDownloader:
    def __init__(self, format="best", outtmpl=Path.cwd()):
        self.format = format
        self.outtmpl = outtmpl

        self.opts = {
            "format": self.format,
            "outtmpl": str(self.outtmpl / "%(title)s.%(ext)s"),
            "quiet": False,
            "noplaylist": True,
            "writethumbnail": True,
            "writesubtitles": False,
            "progress_hooks": [self.progress_hook],
        }

    def progress_hook(self, data):
        if data["status"] == "downloading":
            print(
                f"\r{data['_percent_str']} | "
                f"{data['_speed_str']} | "
                f"ETA: {data['_eta_str']}",
                end=""
            )

        elif data["status"] == "finished":
            print("\n Download Finished!")

    def downloader(self, url):
        with YoutubeDL(self.opts) as ydl:
            ydl.download([url])


if __name__ == "__main__":
    url = "https://youtu.be/R3XIGon2RjY?si=wJyjLrdgcKBg37X0"

    downloader = YutubeDownloader(
        format="worst",
        outtmpl=Path.cwd()
    )

    downloader.downloader(url)
