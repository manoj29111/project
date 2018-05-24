e=input()
f=input()
g=[]
s=0
for i in range(0,e):
    m=input()
    g.append(m)
for i in range(0,len(g)):
    if(g[i]==f):
        s=s+1
print g
print(s)
