import numpy as np
arr = np.random.randint(0, 30, size=(10))
print(arr)

# O(N)
search_item = 15
for i in range(len(arr)):
    if arr[i] == search_item:
        print('Searching '+str(search_item)+' and found! at ' + str(i))
    else:
        print('Searchinng '+str(search_item)+' and did not find at: ' + str(i))
