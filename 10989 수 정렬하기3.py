n = int(input())
l = [0 for _ in range(10001)]
for i in range(n):
    k = int(input())
    l[k-1] += 1
for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            print(i+1)