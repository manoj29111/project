e=input()
f=input()
g=[]
n=1
for i in range(1,e):
    m=input()
    g.append(m)
for i in range(1,len(g)):
    if(g[i]==f):
        n=n+2
print g
print(n)
