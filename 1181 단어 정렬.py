n = int(input())
users = {}

for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age not in users:
        users[age] = []
    users[age].append(name)

sorted_age = sorted(users)
for age in sorted_age:
    for name in users[age]:
        print(age, name)