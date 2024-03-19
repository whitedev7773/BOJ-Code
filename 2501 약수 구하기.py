def find_divisors(N):
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    return divisors

N, K = map(int, input().split())
divisors = find_divisors(N)

if len(divisors) < K:
    print(0)
else:
    print(divisors[K - 1])
