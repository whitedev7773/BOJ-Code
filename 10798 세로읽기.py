lines = []
for _ in range(5):
    lines.append(input())

for j in range(15):
    for ln in lines:
        try:
            print(ln[j], end="")
        except:
            pass