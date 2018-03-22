
def main():
	try:
		g=0
		b=int(input())
		while(b!=0):
			b=b/3
			if b==2:
				g=2
				break
		if g!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
