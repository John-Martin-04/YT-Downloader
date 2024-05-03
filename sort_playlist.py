songs=[]
final=open("Final.txt",'r+',encoding='utf-8')
for line in final:
   songs.append(line)
songs.sort()
final.close()
final=open("Final.txt",'r+',encoding='utf-8')
for line in songs:
   final.write(line)
final.close()