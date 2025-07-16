import sys

num = int(input())
person_list = []

for i in range(num):
    age, name = sys.stdin.readline().split()
    person_list.append((int(age), i, name))

sorted_person = sorted(person_list, key=lambda x: (x[0], x[1]))

for age, _, name in sorted_person:
    print(age, name)