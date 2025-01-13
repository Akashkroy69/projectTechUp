from pytube import YouTube 

def download_video(url,path):
    # Create a YouTube object
    yt = YouTube(url)
    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()
    # Download the video
    stream.download(path)
    print("Downloaded successfully!")

url = input("Enter the URL of the video: ")
download_video(url, r"C:\Users\Lenovo\Downloads")

