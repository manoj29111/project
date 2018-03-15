num=int(input("Enter number:"))
ans=''
while(num!=0):
	t=num%11
	if t%2!=0:
		ans=ans+' '+str(t)
	num=num//11
print("ODD number is",ans[::-1])
