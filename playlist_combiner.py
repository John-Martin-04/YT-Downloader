y=open("My YouTube Library.txt",'r',encoding='utf-8')
s=open("My Spotify Library.txt",'r',encoding='utf-8')
final=open("Final.txt",'r+',encoding='utf-8')

# for line in s:
#    final.write(line)
for line1 in y:
   flag =0
   for line2 in final:
      if line1!=line2:
         flag=1
   if flag==0:
      final.write(line1)
   

y.close()
s.close()
final.close()