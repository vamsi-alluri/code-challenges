def sublist_duplicates(lst):
    sublists = []

    for item in set(lst):
#        print(item)
#        print(lst.count(item))
#        sublists.append([item] * lst.count(item))
        if (lst.count(item)>=2):
            sublists.append(str(item))
        
    return sublists
            
#lst_of_duplicates = [1, 2, 10, 3, 4, 1, 's', 2, 3, 1, 4, 's']
dummy = input()
lst_of_duplicates = [int(x) for x in input().split()]
print(' '.join(sublist_duplicates(lst_of_duplicates)))
