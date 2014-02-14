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
    return bOp_random(c)
    cs=next(c)
    if len(cs)>0:
        return cs[0]
    return c
def genTree(c,n):
    t=treelib.Tree()
    nd=t.create_node(c,gentag())
    if c==1:#leaf
        return t
    if n==0:
        return t
    cs=next(c)
    for child in cs:
        new_tree=genTree(child,n-1)
        t.paste(nd.identifier, new_tree) 
    return t
def E(x):
    pass
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
def VALUE(t,n):
    cids=t[t.root].fpointer
    if len(cids)==0:
        if n% 2==0:
            return 1
        else:
            return -1
    vs=[]
    for cid in cids:
        vs.append(VALUE(t.subtree(cid),n-1))
    if n % 2==0:
        return maxarr(vs)
    else:
        return minarr(vs)
def decsion(t):
    cids=t[t.root].fpointer
    if len(cids)==0:
        return t[t.root].tag #leaf
    des=-100
    for cid in cids:
        v=VALUE(t.subtree(cid),0)
        if des<v:
            des=v
            despath=t[cid]
    return despath.tag
def bOp(c):
    t=genTree(c,2)
    return decsion(t)
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
	
