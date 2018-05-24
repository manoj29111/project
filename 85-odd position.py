ip=input("Enter any String:")
even=''
odd=''
for y in range(1,len(ip)+2):
	if(y%2==1):
		even=even+ip[y-2]
	else:
		odd=odd+ip[y-2]
print(odd," ",even)
