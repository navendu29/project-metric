#file= open("read.txt","r")
#while True :
        #line=file.readline()
        #if not line :
         #   break
        #l=line.rstrip()
        #if l:
            #s=l.replace("class","")
            #m=s.replace("{","")
            #n=m.replace(":","")
            #p=n.replace("public","")

            #r=p.split()
            #print(r)
file= open("test.txt","r")
while True :
    line=file.readline()
    if not line :
        break
    l=line.rstrip()
    if l:
        s=l.replace(":",",")
        m=s.split(",")
        
        print(m)

#def calpub(storage,st,t):
 #   file= open("read.txt","r")
  #  file.seek(t,0)
   # while True :
   #     cur=file.tell()
    #    line=file.readline()
     #   if not line :
      #      break
       # l=line.rstrip()
        #if l:
            
         #   if ('(' in l and ')' in l):
          #          l=l.replace("(","")
           #         l=l.replace(")","")
           #         for item in keywords :
            #            if(item in l):
             #               l=l.replace(item,"")
              #              r=l.split()
               #             v.st.append(r[0]+"()"))

            #if('{'in l):
             #   storage.append('{')
            #if('}' in l):
             #   storage.pop()
            #if (len(storage)==0||"public:"in l):
             #   return (cur)

         

#keywords=["int","char","bool",'float',"void"]
#file= open("read.txt","r")
#while True :
 #       line=file.readline()
  #      if not line :
   #         break
    #    l=line.rstrip()
     #   if l:
      #      if "public:" in l:
       #         t=file.tell()
        #        cur=calpub(storage,"public",t)
         #       file.seek(cur,0)
             
          #  else if "protected:" in l:
           #     t=file.tell()
            #    cur=calpub(storage,"protected",t)
             #   file.seek(cur,0)   
            #else:
             #   if ('(' in l and ')' in l):
              #      l=l.replace("(","")
               #     l=l.replace(")","")
                #    for item in keywords :
                 #       if(item in l):
                  #          l=l.replace(item,"")
                   #         r=l.split()
                    #        v.private.append(r[0]+"()")

                        
                        
                        


#file= open("read.txt","r")
#storage=[]
#count=0
#e2=graph()
#keywords=['int','char','bool','float','void']
#while True :
        #line=file.readline()
        #if not line :
         #   break
        #l=line.rstrip()
       # if l:
          #  list=l.split()
         #   length=len(list)
        #    length=length-1
       #     if(list[0]=="class"):
      #          if('{' in list[length]):
     #               storage.append('{')
    #                l=l.replace("{","")
   #             l=l.replace("class","")
  #              l=l.replace(":","")
#                l=l.replace("public","")
 #               l=l.replace("protected","")
       #         l=l.replace("private","")
        #        l=l.replace(",","")
        #        cl=l.split()
       #         t=file.tell()
      #          for x in cl:
     #               e2.addvertex(x)
    #            cur=calculateattributes(storage,t)
   #             file.seek(cur,0)
