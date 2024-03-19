n, k = map(int, input().split())
scores = list(map(int, input().split()))

# scores.sort(reverse=True)
for i in range(n, -1, -1):
    for j in range(i, n-1):
        if scores[j] < scores[j+1]:
            _temp = scores[j]
            scores[j] = scores[j+1]
            scores[j+1] = _temp

print(scores[k-1])