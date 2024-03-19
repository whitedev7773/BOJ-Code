def find_primes(start, end):
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

M = int(input())
N = int(input())

primes = find_primes(M, N)
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])