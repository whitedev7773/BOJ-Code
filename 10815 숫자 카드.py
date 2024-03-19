# set과 list는 in 검사를 할 때 속도 차이가 있음

n = int(input())
holded_card = set(map(int, input().split()))  # 갖고 있는 카드

m = int(input())
to_check_number = list(map(int, input().split()))  # 있는지 확인할 수들

for n in to_check_number:
    if n in holded_card:
        print(1, end=" ")
    else:
        print(0, end=" ")