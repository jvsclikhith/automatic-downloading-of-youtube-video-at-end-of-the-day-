import datetime
from pytube import YouTube



 
video1 = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(video1)

 
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
print("your video will be downloded ")
ys = yt.streams.get_highest_resolution()

while True:  
    if alaramHour = 23 and alaramMin = 00   
       ys.download()
       print("Download completed!!")
       break