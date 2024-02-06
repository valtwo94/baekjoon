T = int(input())

for _ in range(0, T):
    word = ""
    N, M = input().split()
    n = int(N)
    m = str(M)
    for i in range(0, len(m)):
        for __ in range(0, n):
            word += M[i]
    print(word)