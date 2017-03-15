

class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = [];
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
            break
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
        print(v.noofchildren())



e2=graph()
e2.addvertex("n")
e2.addvertex("m")

e2.addvertex("p")
e2.addvertex("q")

e2.addedge("n","m")
e2.addedge("n","p")

e2.addedge("p","q")
e2.DIT("n")
e2.noofchild("n")
#e2.display()
