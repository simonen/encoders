from pytube import YouTube


def download(link_f):
    youtube_object = YouTube(link_f)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("An error has occurred")

    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
download(link)