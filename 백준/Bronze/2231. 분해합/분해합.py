import sys
import sys

decomp = int(sys.stdin.readline().strip())
length = len(str(decomp))

for i in range(max(decomp - 9 * length, 0), decomp + 1):
    if i + sum(map(int, str(i))) == decomp:
        print(i)
        break
else:
    print(0)
