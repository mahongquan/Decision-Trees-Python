import random
import sys
try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
LeftTop=0
Top=1
RightTop=2
Left=3
Right=4
LeftBottom=5
Bottom=6
RightBottom=7
AllDirection=range(8)
AddDirection=[(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
nodeId=0
spct=4*6
grid=range(5)
for i in range(len(grid)):
	grid[i]=[0] *5
grid[2][2]=-1
grid[1][1]=spct/4
grid[3][3]=spct/4
grid[1][3]=spct/4
grid[3][1]=spct/4
def get_right_serial():
    r=[]
    for y in range(5):
        r.append((4,y))
    return r
def get_left_serial():
    r=[]
    for y in range(5):
        r.append((0,y))
    return r
def get_bottom_serial():
    r=[]
    for x in range(5):
        r.append((x,0))
    return r
def get_direction(x,y,direction):
    (xadd,yadd)=AddDirection[direction]
    x=x+xadd
    y=y+yadd
    if x  in range(5):
        if y in range(5):
            return (x,y)
    return None
def get_left_bottom():
    a=set(get_left_serial())
    b=get_bottom_serial()
    for b1 in b:
        a.add(b1)
    return a
def get_right_bottom():
    a=set(get_right_serial())
    b=get_bottom_serial()
    for b1 in b:
        a.add(b1)
    return a
def link(g,n1,n2):
    (i1,j1)=n1
    (i2,j2)=n2
    nd=str(i1)+","+str(j1)
    nd2=str(i2)+","+str(j2)
    g.add_edge(nd,nd2)
def gen_grid():
    g=nx.Graph()
    for i in range(5):
        for j in range(5):
            nd=str(i)+","+str(j)
            g.add_node(nd)
    for i in range(5):
        for j in range(4):
            nd=str(i)+","+str(j)
            nd2=str(i)+","+str(j+1)
            g.add_edge(nd,nd2)
    for i in range(4):
        for j in range(5):
            nd=str(i)+","+str(j)
            nd2=str(i+1)+","+str(j)
            g.add_edge(nd,nd2)
    lbs=get_left_bottom()
    for one in lbs:
        while True:
            (x,y)=one
            new=get_direction(x,y,RightTop)
            if new<>None:
                link(g,one,new)
                one=new
            else:
                break
    rbs=get_right_bottom()
    for one in lbs:
        while True:
            (x,y)=one
            new=get_direction(x,y,LeftTop)
            if new<>None:
                link(g,one,new)
                one=new
            else:
                break
    nx.draw(g,node_size=700)
    plt.show()
gen_grid()