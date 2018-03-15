num=int(input("Enter any number"))
ans=""
for a in range(1,num+1):
	if num%a==0:
		ans=ans+" "+str(a)
print(ans)
