def gcd(d,e):
    if(e==0):
        return d
    else:
        return gcd(e,d%e)
d=int(input("Enter first number:""\n"))
e=int(input("Enter second number:""\n"))
print(gcd(d,e))
