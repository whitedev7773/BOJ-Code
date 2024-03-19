for _ in range(int(input())):
    dollar = int(input())
    for amount in [25, 10, 5, 1]:
        if dollar <= 0:
            print(0, end=" ")
            continue
        print(dollar//amount, end=" ")
        dollar %= amount
    print("")