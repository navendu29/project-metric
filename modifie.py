#file= open("abc.txt","r")

#print(l)
            #if('(' in l  and  ')'in l):
                #lis=l.split()
                #for item in keywords :
                #    if(lis[0]==item):
               #         method=method+1

#calculates complexity
def cyclomaticcomplexity(s,storage1):
    file =open("xyz.txt","r")
    file.seek(s,0)
    complex=0
    while True:
        ls=file.readline()
        ll=ls.rstrip()
        if ll:
            if '{' in ll:
                storage1.append('{')
            if '}' in ll :
                storage1.pop()
            if len(storage1)>=1:
                if('if' in ll or 'for' in ll or 'while' in ll):
                    complex=complex+1
                    if('&&' in ll or '||' in ll):
                        complex=complex+1
            if len(storage1)==0:
                return complex+1
#calculates attributes and methods in a class
def calculateattributes(storage,t):
    file=open("xyz.txt","r")
    file.seek(t,0)
   # print("helo")
    keywords=['int','char','bool','float','void']
    count=0
    storage1=[]
    method=0
    complexity=0
    while True :
        line=file.readline()
        l=line.rstrip()
        if l :
            if ('(' in l and ')' in l and ';' not in l):
                lis=line.split()
                for item in keywords :
                    if(lis[0]==item):
                            method=method+1
                            if('{' in l):
                                storage1.append('{')
                            pos=file.tell();    
                            complexity=complexity+cyclomaticcomplexity(pos,storage1)
            if('{'in l):
                storage.append('{')
            if('}' in l):
                storage.pop()
            elif(len(storage) == 1):
                #print(l)
                list=l.split()
                #print(list)
                length=len(list)
                l=length-1
                #print("hello")
                for item in keywords :
                    if(item in list[0]):
                        if(';' in list[l]):
                            #print("yes")
                            count=count+1
            if (len(storage)==0):
                print("NOA",count)
                cur=file.tell()
                print("NOM",method)
                print("WMC",complexity)
                return (cur)
    
file= open("xyz.txt","r")
storage=[]
count=0
keywords=['int','char','bool','float','void']
while True :
        line=file.readline()
        if not line :
            break
        l=line.rstrip()
        if l:
            list=l.split()
            length=len(list)
            length=length-1
            if(list[0]=="class"):
                if('{' in list[length]):
                    storage.append('{')
                t=file.tell()    
                cur=calculateattributes(storage,t)
                file.seek(cur,0)
