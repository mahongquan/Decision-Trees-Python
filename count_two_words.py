def count(ju,dic,dic_first):
	ws=ju.split()
	ws2=[]
	for i in range(len(ws)-1):
		ws2.append(ws[i]+" "+ws[i+1])
	for w2 in ws2:
		if dic.get(w2)==None:
			dic[w2]=1
		else:
			dic[w2]+=1
		if dic.get("a life")==2:
			print ws2
			raw_input()
	for w2 in ws2:
		(l,r)=w2.split()
		if dic_first.get(l)==None:
			dic_first[l]=1
		else:
			dic_first[l]+=1
data="""Do you hear the people sing, singing a song of angry men. It is the music of a people, who will not be slaves again, when the beating of your heart echoes the beating of the drums. There is a life about to start when tomorrow comes."""
data=data.replace(',','.')
jus=data.split('.')
dic={}
dic_first={}
ws2=[]
for ju in jus:
	count(ju,dic,dic_first)
out=[]
for k in dic:#output
	(l,r)=k.split()
	print k,dic[k],dic_first[l]
	n=dic[k]/float(dic_first[l])
	out.append([n,k])
out.sort()
for o in out:
	print o[0],o[1]
