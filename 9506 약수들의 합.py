def find_divisors(N):
    divisors = []
    for i in range(1, N):
        if N % i == 0:
            divisors.append(i)
    return divisors

while True:
    n = int(input())
    if n == -1:
        break

    divisors = find_divisors(n)
    if n == sum(divisors):
        print(n, "=", " + ".join(map(str, divisors)))
    else:
        print(n, "is NOT perfect.")