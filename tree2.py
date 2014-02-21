try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
def showTree(t):
    g=nx.DiGraph()
    t.digraph(g)
    nlarge=[n for n in g.nodes() if g.node[n]['level'] <>0]
    nroot=[n for n in g.nodes() if g.node[n]['level'] ==0]
    pos=nx.spring_layout(g) # positions for all nodes
    # edges
    nx.draw_networkx_edges(g,pos)
    # nodes
    nx.draw_networkx_nodes(g,pos,nodelist=nlarge,node_size=700)
    #root
    nx.draw_networkx_nodes(g,pos,nodelist=nroot,node_color='b',node_size=700)
    nx.draw_networkx_labels(g,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    plt.show() # display
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
def test1():
    n1=TreeNode(1)
    n2=TreeNode(2)
    n1.add_child(n2)
    n3=TreeNode(3)
    n1.add_child(n3)
    n4=TreeNode(4)
    n2.add_child(n4)
    n5=TreeNode(5)
    n2.add_child(n5)
    n60=TreeNode(60)
    n5.add_child(n60)

    n6=TreeNode(6)
    n7=TreeNode(7)
    n6.add_child(n7)
    n8=TreeNode(8)
    n6.add_child(n8)
    n9=TreeNode(9)
    n7.add_child(n9)

    n5.add_child(n6)
    showTree(n1)
def test2():
    pass
if __name__=="__main__":
    test1()
