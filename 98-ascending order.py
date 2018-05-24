def changed():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(3,n):
		if l[i-3]>l[i]:
			print(l[i-3])
			break
try:
	changed()
except:
	print('invalid')             
	
	
