num=int(input(99))
h=0
for x in range(1,num+1):
	if(num%x==0):
		h=h+1
if(h>2):
	print("composite")
else:
        print("Not composite")
