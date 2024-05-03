songs=[]
final=open("Final.txt",'r',encoding='utf-8')
for line in final:
   songs.append(line)
final.close()
final=open("Final2.txt",'w',encoding='utf-8')

for i in range(0,len(songs)):
   line=songs[i]
   for j in range(i+1,len(songs)) :
      if i>len(songs)-1:
         break
      next=songs[j]
      if next in line:
         # final.write(line)
         print(next)
         break
   
final.close()