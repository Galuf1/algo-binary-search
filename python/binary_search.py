def binary_search(val, array):

    sorted_array = sorted(array)
    print(sorted_array)
    if (len(sorted_array))%2 == 0:
        middle = round(len(sorted_array)/2) - 1
    else:
        middle = int(len(sorted_array)/2)

    if sorted_array[middle] == val:
        return middle
    elif len(sorted_array) == 1:
        return -1
    elif val < sorted_array[middle]:
        return binary_search(val,sorted_array[:middle])
    else:
        return binary_search(val,sorted_array[middle+1:])  

print(binary_search(19,[1,2,3,19,9,4,6,7,8]))
'''
- sort the array
- find the middle of the array
- if middle = value return index
***recursive***
- else if it's not equal then middle split array


val = 2
[1,2,3,4,5,6,7,8,9] len(array)/2

# '''
# array = [10,20,30,40,50,60,70,80,90,100]  
# print(round(len(array)/2))

