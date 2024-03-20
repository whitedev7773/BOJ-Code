def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // _gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))