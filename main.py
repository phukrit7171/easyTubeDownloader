from pytube import YouTube
link = input("YouTube Link: ")
output_name = input("Video Output Name: ")+".mp4"
print("Downloading please wait ...")
SAVE_PATH = ""
try:yt = YouTube(link)
except:print("Connection Error")
mp4_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
if mp4_stream:
    try:
        mp4_stream.download(output_path=SAVE_PATH, filename=output_name)
        print("Download completed successfully.")
    except:
        print("Error downloading the video.")
else:
    print("No mp4 streams available for this video.")
