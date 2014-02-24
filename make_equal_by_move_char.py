def getBeforeOrlast(stra,c):
	at=getcharIndex(stra,c)
	r=(at-1) % len(stra)
	return stra[r]
def getcharIndex(str1,char):
	for i in range(len(str1)):
		if char==str1[i]:
			return i
	return None
def changeB(strb,char):#move the find char to head
	at=getcharIndex(strb,char)
	strb=strb[:at]+strb[at+1:]
	return char+strb
s1="bcad"
s2='abcd'
while s1<>s2:
	char=getBeforeOrlast(s1,s2[0])#find the char in destination string that is before first char in source string
	s2=changeB(s2,char)
	print s1,s2
	#raw_input()