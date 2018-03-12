def smallest_of( list ):
    min = list[ 0 ]
    for x in list:
        if x < min:
            min = x
    return min
print(smallest_of([12,5,15,8,4,24,6,12]))
