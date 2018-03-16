def maxl(m):
	max=0
	for i in m:
		if max<i:
			max=i
	print(max)
def main():
	try:
		m=[1,2,3,5,4,47,4,24,64,4]
		maxl(m)
	except:
		print('invalid')
main()
