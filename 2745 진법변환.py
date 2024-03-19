"""
N진수 -> 10진수 변환 규칙

ex) 5진수 324를 10진수로 변환
1. 각 자리수를 10진수로 변환
    3(5진수) = 3(10진수)
    2(5진수) = 2(10진수)
    4(5진수) = 4(10진수)
2. 변환된 각 자리수 * 5(진수)**해당 자리의 왼쪽 기준 위치 => 모두 더하기.
    (3 * 5^2) + (2 * 5^1) + (4 * 5^0) = (3 * 25) + (2 * 5) + (4 * 1) = 75 + 10 + 4
"""

N, B = input().split()
B = int(B)

result = 0
pow = 0
for pos in reversed(N):
    if pos.isdigit():
        result += int(pos) * (B ** pow)
    else:
        result += (ord(pos.upper()) - 55) * (B ** pow)
    pow += 1

print(result)
