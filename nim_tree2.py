import random
import sys
try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
class TreeNode:
    def __init__(self,value):#value is used here,node is used other places
        self.parent=None
        self.value=value
        self.children=[]
    def add_child(self,n):
		n.parent=self
		self.children.append(n)
    def digraph(self,g):
       if self.parent==None:
           g.add_node(self.value,level=0)
       for c in self.children:
           g.add_node(c.value,level=1)
           g.add_edge(self.value,c.value)
           c.digraph(g)
    def getroot(self):
    	if self.parent==None:
    		return self
    	return self.parent.getroot()
def next(c):#next state
    if(c>3):
        return [c-1,c-2,c-3]
    elif (c>2):
        return [c-1,c-2]
    elif (c>1):
        return [c-1]
    else:
        return []
def aOp(c):#A decide
    t=genTree(c,20)
    return decsion(t)
    #return op_random(c)
def genTree(c,n): #current state to tree
    t=TreeNode(c)
    if c==1:#leaf
        return t
    if n==0:
        return t
    cs=next(c)
    for child in cs:
        new_tree=genTree(child,n-1)
        t.add_child(new_tree) 
    return t
def maxarr(v):
    v0=-100
    for v1 in v:
        if v1>v0:
            v0=v1
    return v0
def minarr(v):
    v0=1000000
    for v1 in v:
        if v1<v0:
            v0=v1
    return v0
def VALUE(t,n): #value tree
    cids=t.children
    if len(cids)==0:
        if n% 2==0:
            return 1
        else:
            return -1
    vs=[]
    for cid in cids:
        vs.append(VALUE(cid,n-1))
    if n % 2==0:
        return minarr(vs)
    else:
        return maxarr(vs)
def decsion(t): #decide according to value of subtrees
    cids=t.children
    if len(cids)==0:
        return t.value #leaf
    des=-100
    despath=None
    for ctree in cids:
        v=VALUE(ctree,0)
        if des<v:
            des=v
            despath=ctree.value#path
    return despath
def bOp(c):#B decide
    t=genTree(c,20)
    return decsion(t)
def op_random(c):#decide random 
    cs=next(c)
    n=len(cs)
    if n>0:
        at=random.randint(0,n-1)
        return cs[at]
    return c
def main(): #state sequence by first path
    c0=6
    cur=c0
    while True:
        cs=next(cur)
        if len(cs)>1:
            print cs[0]
            cur=cs[0]
        else:
            break
    pass
def main2(): #A B decide turn by turn
    c0=int(sys.argv[1])
    g=nx.DiGraph()
    g.add_node(c0)
    print "begin num="+str(c0)
    cur=c0
    aturn=True
    while True:
        if aturn:
            new=aOp(cur)
            if new!=cur:
                print "A remove:"+str(cur-new)+",left:"+str(new)
                g.add_edge(cur,new,weight=1)
                cur=new
                aturn=False
            else:
                print "A lose"
                break
        else:
            new=bOp(cur)
            if new!=cur:
                print "B remove:"+str(cur-new)+",left:"+str(new)
                g.add_edge(cur,new,weight=2)
                cur=new
                aturn=True
            else:
                print "B lose"
                break
    showG(g)
def showG(g):
    elarge=[(u,v) for (u,v,d) in g.edges(data=True) if d['weight'] >1.5]
    esmall=[(u,v) for (u,v,d) in g.edges(data=True) if d['weight'] <=1.5]
    pos=nx.spring_layout(g) # positions for all nodes
# nodes
    nx.draw_networkx_nodes(g,pos,node_size=700)
# edges
    nx.draw_networkx_edges(g,pos,edgelist=elarge,width=6)
    nx.draw_networkx_edges(g,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='b',style='dashed')
    nx.draw_networkx_labels(g,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    plt.show() # display
main2()
    
