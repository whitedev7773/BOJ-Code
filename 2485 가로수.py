from math import gcd
arr = []

N = int(input())

a = int(input())
for i in range(N-1):
    num = int(input())
    arr.append(num - a)
    a = num

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

count = 0
for each in arr:
    count += each // g - 1

print(count)