N = int(input())

max_5kg_bags = N // 5

while max_5kg_bags >= 0:
    remaining_sugar = N - (max_5kg_bags * 5)
    if remaining_sugar % 3 == 0:
        min_3kg_bags = remaining_sugar // 3
        print(max_5kg_bags + min_3kg_bags)
        break
    max_5kg_bags -= 1  # 3kg로 못 맞추면 5kg 하나 빼기
else:
    print(-1)
