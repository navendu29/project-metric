file= open("xyz.txt","r")


count=0
while True:
    c = file.readline()
    if not c:
        break
    pos=file.tell()
    print (pos)
    count=count+1
print(count)    
    
