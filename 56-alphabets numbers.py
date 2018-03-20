a=input()
e=0
l=0
for b in a:
    if(b.isalpha()):
       e=e+1
    if(b.isdigit()):
        l=l+1
    if(e>1 and l>1):
        print "yes"
        break
else:
    print "no"
