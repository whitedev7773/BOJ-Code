N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= M and current_sum > result:
                result = current_sum

print(result)