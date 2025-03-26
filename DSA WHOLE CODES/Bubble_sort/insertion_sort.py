def bubble_sort(my_list):
    for i in range((len(my_list)-1),0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list


print(bubble_sort([4,2,6,5,1,3]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]))
print(bubble_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]))

print(selection_sort([4,2,6,5,1,3]))
print(selection_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(selection_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
print(selection_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]))
print(selection_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))

print(insertion_sort([4,2,6,5,1,3]))
print(insertion_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(insertion_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
print(insertion_sort([4,2,6,5,1,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """