import numpy as np
#arr = np.random.randint(0, 30, size=(10))
arr = np.random.choice(20, 10, replace=False)
print(arr)

# Binary Search works by searching an array by halving it each time.

arr = sorted(arr)
print('Sorted Array: '+str(arr))

# Implementing Binary Search


def bin_search(arr, element):

    if len(arr) % 2 == 1:
        center_index = (len(arr) + 1) // 2
        #print(center_index,arr)
    else:
        center_index = (len(arr)) // 2
        #print(center_index, arr)
    if len(arr) == 1 and arr[0] != element:
        print('Did not find!')
    else:
        if len(arr)>1 and arr[center_index] == element:
            print('Found {} at {} of {}'.format(element, center_index, arr))
        elif(element < arr[center_index]):
            bin_search(arr[0:center_index], element)
        elif(element > arr[center_index]):
            bin_search(arr[center_index:len(arr)], element)
    


bin_search(arr, 15)
