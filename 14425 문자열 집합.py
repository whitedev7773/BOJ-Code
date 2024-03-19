s_count, m = map(int, input().split())
s = set()

count = 0

for _ in range(s_count):
    s.add(input())

for _ in range(m):
    if input() in s:
        count += 1

print(count)