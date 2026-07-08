# YouTube Downloader

A simple YouTube downloader implemented in Python using two different libraries:

- **yt-dlp** (recommended)
- **pytube** (legacy implementation)

The project is intended for learning and comparing the APIs of both libraries.

---

## Requirements

Python 3.10+

Install the required libraries:

```bash
pip install yt-dlp
pip install pytube
```

---

## yt-dlp Example

```python
from yt_dlp_downloader import YutubeDownloader

downloader = YutubeDownloader(format="best")
downloader.downloader(
    "https://youtu.be/R3XIGon2RjY"
)
```


---

## pytube Example

```python
from pytube_downloader import YouTubeDownloader

downloader = YouTubeDownloader()
downloader.download(
    "https://youtu.be/R3XIGon2RjY"
)
```

---

## Features

### yt-dlp

- Download videos
- Choose video quality
- Download thumbnail
- Progress display
- Prevent playlist downloads

### pytube

- Download videos
- Select resolution
- Save to custom directory

---

## Notes

- `yt-dlp` is actively maintained and recommended.
- `pytube` may stop working whenever YouTube changes its API.

---
