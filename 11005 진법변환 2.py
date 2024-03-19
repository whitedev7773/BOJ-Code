N, B = map(int, input().split())

result = ""
while N > 0:
    remainder = N % B
    if remainder >= 10:
        result = chr(ord('A') + remainder - 10) + result
    else:
        result = str(remainder) + result
    N //= B

print(result)