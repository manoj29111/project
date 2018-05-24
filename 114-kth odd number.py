a=input()
k=input()
e=[]
f=[]
for x in range(0,a):
    n=input()
    e.append(n)
for i in e:
    if i%5!=0:
        f.append(i)
        f.sort()
print f 
print f[k-2]
