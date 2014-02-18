try:
    import matplotlib.pyplot as plt
except:
    raise 
import networkx as nx
def showTree(g):
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
class Tree(nx.DiGraph):
	def __init__(self,root):
		super(Tree,self).__init__()
		self.root=root
		self.add_node(root,level=0)
	def add_child(self,a,b):
		pnode=self.node[a]
		self.add_node(b,level=pnode['level']+1)
		self.add_edge(a,b)
	def get_child(self,a):
		es=self.out_edges(a)
		for  e in es:
			print type(e),e,dir(e)
		raw_input()
g=Tree(1)
g.add_child(1,2)
g.add_child(1,2)
g.add_child(1,3)
g.add_child(2,4)
g.add_child(2,5)
g.get_child(2)
raw_input()
showTree(g)
