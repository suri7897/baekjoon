import sys

num = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))
max_score = max(score)
new_scores = [(s / max_score) * 100 for s in score]

print(sum(new_scores)/num)
