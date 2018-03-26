x=input()
y=input()
p=[]
for i in range(0,x):
    s=input()
    p.append(s)
    p.sort()
print(p[y-1])
