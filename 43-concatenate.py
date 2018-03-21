def compare(str1,str2):
	for i in range(len(str2)):
		str1+=str2[i]
	print(str1)
def main():
	try:
		m1=input()
		m2=input()
		compare(m1,m2)
	except:
		print('hello world')
main()
