def countd(m,a):
	(max,min)=(0,9998)
	for i in range(a):
		if max<m[i]:
			max=m[i]
		if min>m[i]:
			min=m[i]
	print(min,max)
def main():
	try:
		m=[]
		a=int(input())
		for i in range(a):
			m.append(int(input()))
		countd(m,a)
	except:
		print('invalid')
main()
