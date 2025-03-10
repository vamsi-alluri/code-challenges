# Initializing list
n,m           = [int(x) for x in input().split()]
test_list_set = [int(x) for x in input().split()]
test_array    = [int(x) for x in input().split()]

if m <= n:
    #Checking if 4 exists in list ( using set() + in )  
    # using set() + in
    f = 0 #initializing flag as 0 i.e no same elements 
    test_list_set = set(test_list_set)
    for i in test_array:
        if i in test_list_set : #if two elements are equal the there is a subset
            f = 1
        else:
            f = 0
    if ( f == 1 ):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
