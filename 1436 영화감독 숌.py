# 영화 망해라 걍

n = int(input())
count = 0

number = 665

while True:
    if count == n:
        break
    number += 1
    if '666' in str(number):
        count += 1

print(number)