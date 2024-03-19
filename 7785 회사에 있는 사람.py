n = int(input())
in_company = set()

for i in range(n):
    name, status = input().split()
    if status == "enter":
        in_company.add(name)
    elif status == "leave":
        in_company.remove(name)

print("\n".join(list(sorted(in_company, reverse=True))))