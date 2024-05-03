from youtube_search import YoutubeSearch
import time
query=[]
final=open("Final.txt",'r',encoding='utf-8')

for line in final:
   query.append(line)
for line in query:
   print(line)
final.close()
url=""
links=open("links.txt",'r+',encoding='utf-8')
for i in range(0,len(query)):
   results = YoutubeSearch(query[i], max_results=1).to_dict()
   for result in results:
      url = f"https://youtube.com{result['url_suffix']}"
   links.write(url+"\n")
   print( i,"  done")