N, M = map(int, input().split())
numbers = []
str = ""
for _ in range(1, N + 1):
    numbers.append(0)
for _ in range(1, M + 1):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        numbers[x] = k
for i in range(0, N):
    if i != 0:
        str += " "
    str += f"{numbers[i]}"
print(str)
