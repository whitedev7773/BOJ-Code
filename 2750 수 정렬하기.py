n = int(input())

target = []

for _ in range(n):
    target.append(int(input()))

# 귀찮으면 걍 target.sort() 해도 됨
for i in range(n, -1, -1):
    for j in range(i, n-1):
        if target[j] > target[j+1]:
            _temp = target[j]
            target[j] = target[j+1]
            target[j+1] = _temp

print("\n".join(map(str, target)))