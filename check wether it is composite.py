num=int(input("2"))
flag=0
for x in range(1,num+1):
	if(num%x==0):
		flag=flag+1
if(flag>2):
	print("composite")
else:
        print("Not composite")
