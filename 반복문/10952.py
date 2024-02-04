import sys

while 1:
    A, B = map(int, sys.stdin.readline().split())

    if A + B != 0:
        print(A + B)
    else:
        break
