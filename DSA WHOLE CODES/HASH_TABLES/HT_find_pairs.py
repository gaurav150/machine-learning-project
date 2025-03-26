def find_pairs(arr1,arr2,target):
    y = set(arr1)
    result = []
    for ele in arr2:
        complement = target - ele
        if complement in y:
            result.append((complement,ele))
    return result
            


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""