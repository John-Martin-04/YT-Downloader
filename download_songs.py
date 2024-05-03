# from pytube import YouTube
# links=open("links.txt",'r',encoding="utf-8")
# link=[]
# fin=open("fin.txt",'w',encoding="utf-8")
# links.seek(0)

# resolution=["1080","720p"]

# for line in links:
#    link.append(line)

# for l in link:
#    video = YouTube(l, on_progress_callback=on_progress, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
#    r=resolution[0]
#    i=0
#    while (True) :
#       down=video.streams.filter(res=r).first()
#       if down:
#          fin.write(YouTube(l).title+"\n")
#          down=video.streams.filter(res=r).first()
#          down.download("E:/mus")
#          break
#       else:
#          i+=1
#          if i>1:
#             print("Could not download",YouTube(l).title,"\n")
#             break
#          r=resolution[i]

   
 

# fin.close()
# links.close()

from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    progress = (1 - bytes_remaining / stream.filesize) * 100
    print(f"Downloading... {progress:.2f}% complete", end="\r")

def download_video(video, output_path):
    try:
        # Get the highest resolution stream that includes both video and audio
        stream = video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

        if stream:
            stream.download(output_path)
            print(f"Downloaded: {video.title} in {stream.resolution}")
        else:
            print(f"Could not download {video.title}")
    except Exception as e:
        print(f"Error downloading {video.title}: {str(e)}")

links_file = open("links.txt", 'r', encoding="utf-8")
links = links_file.readlines()
fin = open("fin.txt", 'w', encoding="utf-8")

output_path = "E:/mus"

for l in links:
    try:
        video = YouTube(l, on_progress_callback=on_progress)
        download_video(video, output_path)
    except Exception as e:
        print(f"Error processing {l}: {str(e)}")

fin.close()
links_file.close()