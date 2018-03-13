num=int(input("Enter any Number:"))
ans=0
while(num!=0):
	y=num%10
	ans=ans*10+y
	num=num//10
print(ans)
