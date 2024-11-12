def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partitionIndex(arr, low, high):
    pivot = arr[low]
    left = low+1
    right = high

    while(left<right):
        while(arr[left]<pivot and left<=high):
            left += 1

        while(arr[right]>pivot and right>=low):
            right -= 1

        if(left<right):
            swap(arr, left, right)

    swap(arr, low, right)
    return right

def quickSort(arr, low, high):
    if(low<high):
        pIndex = partitionIndex(arr, low, high)
        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)

arr = [4, 7, 2, 8, 5, 9, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)