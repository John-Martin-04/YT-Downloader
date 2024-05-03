from youtube_search import YoutubeSearch
import time
import threading
from pytube import YouTube
from queue import Queue

def search_and_write_results(queries, results_queue):
    for query in queries:
        result = YoutubeSearch(query, max_results=1).to_dict()
        for item in result:
            url = f"https://youtube.com{item['url_suffix']}"
            results_queue.put(url)

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

yt=open("My YouTube Library.txt",'r',encoding='utf-8')
spotify=open("My Spotify Library.txt",'r',encoding='utf-8')
with open("songlist.txt",'w'):
   pass
songlist=open("songlist.txt",'r+',encoding='utf-8')

#reads spotify playlist and writes to o/p file songlist
for line in spotify:
   songlist.write(line)
spotify.close()

#if song is in yt list but not iin spotify list add to o/p file songlist
for line1 in yt:
   flag =0
   for line2 in songlist:
      if line1!=line2:
         flag=1
   if flag==0:
      songlist.write(line1)
yt.close()

#sort the songs in ascending order names
songlist.seek(0)
songs=[]
for line in songlist:
   songs.append(line)
songs.sort()
songlist.seek(0)
for line in songs:
   songlist.write(line)

#now remove duplicate songs
songlist.close()
for i in range(0,len(songs)):
   line=songs[i]
   for j in range(i+1,len(songs)) :
      if i>=len(songs):
         break
      if songs[j] in line:
         songs[j]+="$delete"
         print(songs[j])
         break
with open("songlist.txt",'w',encoding='utf-8') as songlist:
   for i in songs:
      if"$delete" not in i:
         songlist.write(i)

#create yt links for the songs
query=[]
with open("songlist.txt",'r',encoding='utf-8') as songlist:
   queries = [line.strip() for line in songlist]
url=""
results_queue = Queue()

# Number of threads to use
num_threads = 8

# Split queries into chunks for each thread
chunks = [queries[i:i + len(queries) // num_threads] for i in range(0, len(queries), len(queries) // num_threads)]

# Create and start threads
threads = []
for chunk in chunks:
    thread = threading.Thread(target=search_and_write_results, args=(chunk, results_queue))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Write search results to links.txt
with open('links.txt', 'w', encoding='utf-8') as links:
    while not results_queue.empty():
        links.write(results_queue.get() + "\n")

print("All links generated successfully.")

#download the songs
with open("links.txt", 'r', encoding="utf-8") as links_file:
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
