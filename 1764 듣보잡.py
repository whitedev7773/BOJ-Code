# 빠른 채점을 위해 PyPy3로 제출
# set로 묶고 and(&) 연산

n, m = map(int, input().split())
no_hear, no_see = set(), set()

for _ in range(n):
    no_hear.add(input())
for _ in range(m):
    no_see.add(input())

no_hear_no_see = no_hear & no_see
print(len(no_hear_no_see))
print("\n".join(sorted(no_hear_no_see)))