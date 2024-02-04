N = int(input())
for i in range(0, N):
    str = ""

    for _ in range(1, N - i):
        str += " "

    for __ in range(0, i ):
        str += "*"

    str += "*"
    print(str)
