import math

start, end = map(int, input().split())

for i in range(start, end+1):
    if i < 2:
        continue 
    if i == 2:
        print(i)
        continue
    if i % 2 == 0:
        continue

    is_prime = True
    for j in range(3, int(math.sqrt(i))+1, 2):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)