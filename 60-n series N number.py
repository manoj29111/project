m = int(input("\nEnter the Range:\n"))
i = 0
m1 = 1
m2 = 1
while(i <m):
           if(i <= 2):
                      Next = i
           else:
                      Next =m1 + m2
                      m1= m2
                      m2= Next
           print(Next)
           i =i+1
