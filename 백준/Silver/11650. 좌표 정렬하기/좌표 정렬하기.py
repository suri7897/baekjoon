import sys

num = int(input())
coordinates = []

for i in range(num):
    x, y = sys.stdin.readline().split()
    coordinates.append((int(x), int(y)))

sorted_coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))

for x,y in sorted_coordinates:
    print(x, y)