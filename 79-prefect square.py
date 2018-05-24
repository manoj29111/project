num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
flag=2
prod=num1*num2
for y in range(1,max(num1,num2)+1):
	m=y*y
	if m==prod:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")
