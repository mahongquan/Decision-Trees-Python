import math
try:
    import matplotlib.pyplot as plt
except:
    raise
def circle(x,y,r):
	xarr=[]
	yarr=[]
	for i in range(20):
		jiao=float(i)/20*2*math.pi
		x1=x+r*math.cos(jiao)
		y1=y+r*math.sin(jiao)
		xarr.append(x1)
		yarr.append(y1)
	print xarr
	print yarr
	plt.plot(xarr,yarr,linestyle='-', marker='o', color='r',markersize=10)
	plt.show() # display
circle(5,5,5)