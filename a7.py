def has7(n):
	if (n % 7 ==0):
		return True
	if "7" in str(n):
		return True
def lian7(m):
	at=1
	while(True):
		suc=True
		for i in range(at,at+m):
			if has7(i):
				continue
			else:
				suc=False
				break
		if suc:
			return at
		at+=1
print lian7(11)
