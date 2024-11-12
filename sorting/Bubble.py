def Bubble_Sort(list):
    size = len(list)
    for i in range(0,size-1):
        for j in range(0, size-i-1):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

arr = [4, 7, 2, 8, 5, 9, 1]
Bubble_Sort(arr)
print(arr)