A, B, V = map(int, input().split())

total_height = V - A
daily_progress = A - B

days = total_height / daily_progress
days = int(days) if days.is_integer() else int(days) + 1

print(days + 1)