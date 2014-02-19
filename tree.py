try:
    import matplotlib.pyplot as plt
except:
    raise 
import networkx as nx
def showTree(t):
    g=t.graph
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
class Tree:
	def __init__(self,root=None):
		self.graph=nx.DiGraph()
		if root!=None:
			self.root=root
			self.graph.add_node(root,level=0)
		else:
			self.root=None
	def set_graph(self,g):
		self.graph=g
	def set_root(self,rt):
		if self.root!=None:
			pnode=self.graph.node[self.root]
			pnode['level']=1
		self.root=rt
		pnode=self.graph.node[self.root]
		pnode['level']=0
	def add_child(self,a,b):
		pnode=self.graph.node[a]
		self.graph.add_node(b,level=pnode['level']+1)
		self.graph.add_edge(a,b)
	def get_child(self,a):
		es=self.graph.out_edges(a)
		r=[]
		for  e in es:
			r.append(e[1])#print type(e),e,dir(e)
		return r
	def get_houdai(self,a):
		es=self.graph.out_edges(a)
		r=[]
		for  e in es:
			r.append(e[1])#print type(e),e,dir(e)
			r+=self.get_houdai(e[1])
		return r
	def add_tree(self,a,t):
		r=t.root
		self.add_child(a,r)
		pnode=self.graph.node[r]
		pnode['level']=1
		sts=t.get_subtrees(r)
		for st in sts:
			#showTree(st)
			self.add_tree(r,st)
			#showTree(self)
	def get_subtrees(self,a):
		cs=self.get_child(a)
		sts=[]
		for c in cs:
			sts.append(self.get_tree(c))
		return sts
	def get_tree(self,a):
		cs=self.get_houdai(a)
		cs.append(a)
		g1=self.graph.copy()
		g=g1.subgraph(cs)
		t=Tree()
		t.set_graph(g)
		t.set_root(a)
		return t
def test1():
	g=Tree(1)
	g.add_child(1,2)
	g.add_child(1,2)
	g.add_child(1,3)
	g.add_child(2,4)
	g.add_child(2,5)
	g.add_child(5,60)
	#print g.get_childs(2)
	#st=g.get_tree(2)
	#showTree(st)
	#showTree(g)
	#raw_input("pause")
	g2=Tree(6)
	g2.add_child(6,7)
	g2.add_child(6,8)
	g2.add_child(7,9)
	g.add_tree(5,g2)
	showTree(g)
def test2():
	pass
if __name__=="__main__":
    test1()