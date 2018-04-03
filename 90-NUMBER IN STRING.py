k=input()
c=[]
for i in range(0,len(k)):
   if(k[i].isdigit()):
       c.append(k[i])
d="".join(c)
print d
