n = list(map(int, list(input())))

n.sort(reverse=True)
print("".join(map(str, n)))