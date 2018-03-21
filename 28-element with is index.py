n=int(input("Enter the size"))
h=list(map(int,input("Enter the values").split(' ')))
for x in h:
    print(x,h.index(x))
