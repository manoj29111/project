try:
	d1=int(input())
	d2=int(input())
	while(d2!=0):
		t=d2
		d2=d1%d2
		d1=t
	print(d1)
except:
	print('invalid')
