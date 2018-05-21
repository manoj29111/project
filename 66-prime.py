c = int(input("Enter any number: "))
if c > 1:
    for i in range(4, c):
        if (c % i) == 0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
