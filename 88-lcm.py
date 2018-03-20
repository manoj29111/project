def lcm(m, n):
   if m > n:
       s = m
   else:
       z = n

   while(True):
       if((s % m == 0) and (s % n == 0)):
           lcm = s
           break
       s += 1
    return lcm
print(lcm(5, 6))
