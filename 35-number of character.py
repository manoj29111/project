def main():
	m=input()
	a=0
	for i in m:
		if i.isalpha() :
			a=a+1
	print('No of numerics in a string is :%d'%a)
main()
