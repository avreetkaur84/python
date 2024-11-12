def Selection_Sort(list):
    size = len(list)
    for i in range(0, size-1):
        index_min = i
        for j in range(i+1, size):
            if(list[j]<list[index_min]):
                index_min = j
        temp = list[i]
        list[i] = list[index_min]
        list[index_min] = temp

arr = [4, 7, 2, 8, 5, 9, 1]
Selection_Sort(arr)
print(arr)