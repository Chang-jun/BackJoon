## 빠른 A + B ##
import sys

a = int(sys.stdin.readline().rstrip())

for i in range(1,a+1):
    b, c= map(int, sys.stdin.readline().rstrip().split())
    print(b+c)

