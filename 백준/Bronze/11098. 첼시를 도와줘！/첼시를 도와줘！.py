num_cases = int(input())

answer = []

for i in range(num_cases):
    num_players = int(input())
    price = 0
    name = ''
    for j in range(num_players):
        a,b = input().split()
        if(price < int(a)):
            price = int(a)
            name = b
    answer.append(name)

[print(name) for name in answer]
    