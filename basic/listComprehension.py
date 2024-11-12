list=[1,2,3,4,5]
even = [x for x in list if x%2==0]
# print(even)

a=["st", 1, "av", 3, "ab", 4]
a=[x for x in a if type(x)==int]
# print(a)

def average(list):
    s = sum(list)
    average = sum(list)/len(list)
    print(average)

# average(list)

def multiples(k):
    multiple=[]
    for i in range(1,6):
        mul = i*k
        multiple.append(mul)
    print(multiple)

# multiples(3)