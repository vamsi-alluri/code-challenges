def sublist_duplicates(lst):
    sublists = []

    for item in set(lst):
        if (lst.count(item)>=2):
            sublists.append(str(item))
        
    if not sublists:
        print("unique")
    else:
        print(" ".join(sublists))
            

dummy = input()
lst_of_duplicates = [int(x) for x in input().split()]
sublist_duplicates(lst_of_duplicates)
