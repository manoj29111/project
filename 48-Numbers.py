def avg(m,d):
	sum=0
	for i in range(d):
		sum+=m[i]
	print(sum/d)
def main():
	try:
		d=int(input())
		m=[]
		for i in range(d):
			m.append(int(input()))
		avg(m,d)
	except:
		print('invalid')
main()
