m=[]
n=int(input("Enter Number of Elements:"))
for i in range(1,n+1):
    t=int(input(" "))
    m.append(t)
#x.sort()
print("Median Element is:",m[int((n-1)/2)])
