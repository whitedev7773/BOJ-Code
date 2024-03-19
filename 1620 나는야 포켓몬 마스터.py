# 빠른 채점을 위해 PyPy3로 제출

import sys

input = sys.stdin.readline

pokemon_count, quiz_count = map(int, input().split())
index_to_name = []
name_to_index = {}

for i in range(pokemon_count):
    name = input().rstrip()
    index_to_name.append(name)
    name_to_index[name] = i + 1

for _ in range(quiz_count):
    quiz = input().rstrip()
    if quiz.isdigit():
        key = int(quiz)
        print(index_to_name[key-1])
    else:
        print(name_to_index[quiz])