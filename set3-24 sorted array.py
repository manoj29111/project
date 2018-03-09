m=int(input())
sum=0
num=m
while(num>0):
	r=num%10
	sum=sum*10+r
	num=num/10
print(sum)
