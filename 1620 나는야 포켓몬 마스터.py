pokemon_count, quiz_count = map(int, input().split())
pokemon = set()

for _ in range(pokemon_count):
    pokemon.add(input())

for _ in range(quiz_count):
    quiz = input()
    if quiz in pokemon:
        print(pokemon.index(quiz) + 1)
    else:
        print(pokemon[int(quiz)-1])