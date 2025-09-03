# pip install yt-dlp
from pytubefix import YouTube

url = 'https://www.youtube.com/watch?v=0HyIda5eub8'

yt = YouTube(url=url).streams.get_highest_resolution().download()

print("Successfully Downloaded...!!")

