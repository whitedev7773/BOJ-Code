input()
a = set(input().split())
b = set(input().split())

a_b = a - b
b_a = b - a

print(len(a_b) + len(b_a))