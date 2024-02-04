import sys

N = int(sys.stdin.readline())
for i in range (1 , N+1):
    str = ""
    for _ in range(1, i+1):
        str += "*"
    print(str)