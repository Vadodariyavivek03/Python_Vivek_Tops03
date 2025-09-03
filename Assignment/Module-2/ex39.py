# pip install yt-dlp
from pytubefix import YouTube

url = 'https://www.youtube.com/watch?v=0HyIda5eub8'

yt = YouTube(url=url).streams.get_highest_resolution().download(output_path="Temp_Data")

print("Successfully Downloaded...!!")

# Temp_Data is relative path
# when use this --> r"F:\Tops-Technology\Python_Vivek_Tops03\Assignment\Temp_Data" --> using raw string
# then it will not give error for backslash