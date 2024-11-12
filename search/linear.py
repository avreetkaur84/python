list = [2, 4, 6, 3, 8, 9, 7]
num = 6

def linearSearch(list, num):
    for i in list:
        if(i==num):
            return f"{num} is present at index {list.index(i)}"
        

x = linearSearch(list, num)
print(x)
        
    

def binarySearch(arr, low, high, x):
    while low <= high:
        mid = (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubbleSort():
    print(list)