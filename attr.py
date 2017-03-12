#file= open("abc.txt","r")

#print(l)
            #if('(' in l  and  ')'in l):
                #lis=l.split()
                #for item in keywords :
                #    if(lis[0]==item):
               #         method=method+1  

def calculateattributes(storage):
    file=open("xyz.txt","r")
    print("helo")
    keywords=['int','char','bool','float','void']
    count=0
    method=0
    for line in file:
        l=line.rstrip()
        if l :
            if ('(' in l and ')' in l and ';' not in l):
                lis=line.split()
                for item in keywords :
                    if(lis[0]==item):
                            method=method+1
            if('{'in l):
                storage.append('{')
            if('}' in l):
                storage.pop()
            elif(len(storage) == 1):
                print(l)
                list=l.split()
                print(list)
                length=len(list)
                l=length-1
                print("hello")
                for item in keywords :
                    if(list[0]==item):
                        if(';' in list[l]):
                            print("yes")
                            count=count+1
            if (len(storage)==0):
                print(count)
                print(method)
                return (count)
    



file= open("xyz.txt","r")
storage=[]
count=0
keywords=['int','char','bool','float','void']
for line in file:
        l=line.rstrip()
        if l:
            list=l.split()
            length=len(list)
            length=length-1
            if(list[0]=="class"):
                #if('{' in list[length]):
                    #storage.append('{')
                cur=calculateattributes(storage)
                print(cur)                     
                
