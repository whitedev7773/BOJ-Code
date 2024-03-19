while True:
    case = input()
    if case == "0 0 0":
        break

    a, b, c = map(int, case.split())

    if max(a,b,c) >= sum([a,b,c]) - max(a,b,c):
        print("Invalid")
        continue

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b and b != c and a != c:
        print("Scalene")