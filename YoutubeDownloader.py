from pytube import YouTube

link = 'youtube link here' #PASTE YOUR LINK INSIDE THE QUOTES
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('Your Downloadable folder path here') # PASTE YOUR FOLDER PATH IN WHICH YOU WANT TO DOWNLOAD YOUR VIDEO
print('Download complete')
