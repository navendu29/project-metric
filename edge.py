class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = [];
        self.parent=[]
        self.private=[]
        self.privateattr=[]
        self.protected=[]
        self.protectedattr=[]
        self.public=[]
        self.publicattr=[]
        
    def display(self):
        print (self.name)
        print (self.edges)
    def noofchildren(self):
        return len(self.edges)
    def addedge(self,e):
        self.edges.append(e)
    def getname(self):
        return self.name

class graph:
    def __init__(self):
        self.vertices = [];
    def addvertex(self,name):
        if(self.isvertexpresent(name)=="true"):
            return
        v=Vertex(name)
        self.vertices.append(v)
    def isvertexpresent(self,name):
        for v in self.vertices :
            if (v.getname()==name):
                return "true"
        return "false"    
    def display(self):
        for v in self.vertices:
            print(v.name,"")
            for e in v.edges:
                print(e.name,"")
    def addedge(self,name1,name2):
        v1=self.getvertex(name1)
        v2=self.getvertex(name2)
        
        v1.edges.append(v2)
    def getvertex(self,name1):
        for v in self.vertices:
            if(v.getname()==name1):
                return v
        return null
    def totalclasses(self):
        return len(self.vertices)
    def DIT(self,name):
        for v in self.vertices:
            print("DIT is",self.DIT2(v,name,0))
            
    def DIT2(self,v,name,k):
        if(v.name==name):
            return k
        for edge in v.edges:
            x=self.DIT2(edge,name,k+1)
            if(x!=-1):
                return x
        return -1
    def noofchild(self,name):
        v=self.getvertex(name)
        print("no of child ",v.noofchildren())
    def inheritedmethod(self,name):
        v=self.getvertex(name)
        inherit=0
        for p in v.parent :
            m=p.split()
            inherit=inherit+len(self.getvertex(m[1]).public)+len(self.getvertex(m[1]).protected)
        return inherit
    def inheriteattri(self,name):
        v=self.getvertex(name)
        inherit=0
        for p in v.parent :
            m=p.split()
            inherit=inherit+len(self.getvertex(m[1]).publicattr)+len(self.getvertex(m[1]).protectedattr)
        return inherit
            


#e2=graph()
#e2.addvertex("n")
#e2.addvertex("m")

#e2.addvertex("p")
#e2.addvertex("q")

#e2.addedge("n","m")
#e2.addedge("n","p")

#e2.addedge("p","q")
#e2.DIT("q")
#e2.noofchild("n")


def calculateattributes(storage,t,name,keywords):
    flag="false"
    file= open("read.txt","r")
    file.seek(t,0)
    v=e2.getvertex(name)
    while True :
        line=file.readline()
        if not line :
            break
        l=line.rstrip()
        if l:
            if("protected:" in l):
                flag="protected"
                continue
            if("public:" in l):
                flag="public"
                continue
            if('{'in l):
                storage.append('{')
            if('}' in l):
                storage.pop()
            if (len(storage)==0):
                cur=file.tell()
                return (cur)
            if("(" in l and ")" in l):
                l=l.replace("(","")
                l=l.replace(")","")
                l=l.replace("{","")
                for item in keywords :
                    if(item in l):
                        l=l.replace(item,"")
                r=l.split()
                if(flag=="false"):
                    v.private.append(r[0]+"()")
                elif(flag=="protected"):
                    v.protected.append(r[0]+"()")
                else:
                    v.public.append(r[0]+"()")
            if (len(storage)==1 and '('  not in l and ')'  not in l and ";"in l):       
                  list=l.split()
                  length=len(list)
                  u=length-1
                  for item in keywords :
                      if(item in list[0]):
                          if(';' in list[u]):
                              l=l.replace(";","")
                              l=l.replace(item,"")
                  r=l.split()
                  if(flag=="false"):
                      v.privateattr.append(r[0])
                  elif(flag=="protected"):
                      v.protectedattr.append(r[0])
                  else:
                      v.publicattr.append(r[0])
                              
                            
             

             


file= open("read.txt","r")
storage=[]
count=0
flag=[]
e2=graph()
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
                    l=l.replace("{","")
                    
                if(":" in l):
                    s=l.replace(":",",")
                    m=s.split(",")
                    print(m)
                    
                l=l.replace("class","")
                l=l.replace(":","")
                l=l.replace("public","")
                l=l.replace("protected","")
                l=l.replace("private","")
                l=l.replace(",","")
                cl=l.split()
                t=file.tell()
                u=len(cl)
                i=0
               
                for x in cl:
                    e2.addvertex(x)
                    keywords.append(x)
                for i in range(0,u-1):
                    e2.getvertex(cl[i+1]).edges.append(e2.getvertex(cl[0]))
                    e2.getvertex(cl[0]).parent.append(m[i+1])
                    
                    
                #e2.display()
                #print(keywords)
                cur=calculateattributes(storage,t,cl[0],keywords)
                file.seek(cur,0)
#e2.display()



                
e2.DIT("d")
e2.noofchild("a")
v=e2.getvertex("a")
print("total classes",len(e2.vertices))
print("NOM",len(v.private)+len(v.protected)+len(v.public))
print("NOA",len(v.privateattr)+len(v.protectedattr)+len(v.publicattr))

for v in e2.vertices:
    print(v.name)
    for e in v.edges:
        print(e.name)
    print(v.private)
    print(v.protected)
    print(v.public)
    print(v.privateattr)
    print(v.protectedattr)
    print(v.publicattr)
    print(v.parent)
#h=e2.getvertex("b")
v=e2.getvertex("a")
print("NOM of a",len(v.protected)+len(v.public))
print("NOA of a",len(v.protectedattr)+len(v.publicattr))

v1=e2.getvertex("b")
print("NOM of b",len(v1.protected)+len(v1.public))
print("NOA of b",len(v1.protectedattr)+len(v1.publicattr))

print("inherited methods in c",e2.inheritedmethod("c"))  
print("inherited attributes in c",e2.inheriteattri("c")) 
