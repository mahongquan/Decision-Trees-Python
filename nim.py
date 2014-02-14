import random
import treelib
tagid=0
def gentag():
	global tagid
	tagid+=1
	return str(tagid)
def next(c):
	if(c>3):
		return [c-1,c-2,c-3]
	elif (c>2):
		return [c-1,c-2]
	elif (c>1):
		return [c-1]
	else:
		return []
def aOp(c):
	cs=next(c)
	if len(cs)>0:
		return cs[0]
	return c
def genTree(c,n):
    t=treelib.Tree()
    nd=t.create_node(c,gentag())
    cs=next(c)
    for child in cs:
        new_tree=genTree(child,n-1)
        t.paste(nd.identifier, new_tree) 
    return t
def bOp(c):
    t=genTree(c,5)
    t.show()

def bOp_random(c):
    cs=next(c)
    n=len(cs)
    if n>0:
        at=random.randint(0,n-1)
        return cs[at]
    return c
def main():
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
def main2():
	c0=6
	print "begin num="+str(c0)
	cur=c0
	aturn=True
	while True:
		if aturn:
			new=aOp(cur)
			if new!=cur:
				print "A remove:"+str(cur-new)+",left:"+str(new)
				cur=new
				aturn=False
			else:
				print "A lose"
				break
		else:
			new=bOp(cur)
			if new!=cur:
				print "B remove:"+str(cur-new)+",left:"+str(new)
				cur=new
				aturn=True
			else:
				print "B lose"
				break
main2()
	
