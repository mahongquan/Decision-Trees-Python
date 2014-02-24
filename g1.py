#!/usr/bin/env python
"""
Draw a graph with matplotlib.
You must have matplotlib for this to work.
"""
try:
    import matplotlib.pyplot as plt
except:
    raise 
    
import networkx as nx
class Tree(nx.Graph):
	def __init__(self,data=None, **attr):
		super(Tree,self).__init__(data, **attr)
	def create_node(self,tag,id):
		pass
	
g=Tree()
g.add_nodes_from([2,3])
h=nx.path_graph(10)


nx.draw(g)
plt.savefig("simple_path.png") # save as png
plt.show() # display
