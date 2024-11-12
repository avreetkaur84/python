# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
pos_num = [num for num in numbers if num>0]
# print(pos_num)

# 2. Sum of Even Numbers - using recursion
# Problem: Calculate the sum of even numbers up to a given number n.

def Even_Sum(n):
    if(n==0):
        return 0
    return n+Even_Sum(n-2)

# n = 8
# if(n%2!=0):  n = n-1
# ans = Even_Sum(n)
# print(ans)


# 4. Reverse a String
# Problem: Reverse a string using a loop.
def reverseString(s):
    rs=""
    w=""
    for i in s:
        if(i==" "):
            rs=w+" "+rs
            w=""
        w = w+i
    rs = w+" "+rs
    print(rs)

reverseString("I am a looser")


# PENDING TO TRY
# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.