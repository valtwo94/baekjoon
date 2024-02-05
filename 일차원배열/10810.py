N, M = map(int, input().split())
numbers = []
for _ in range(1, N + 1):
    numbers.append(0)
for _ in range(1, M + 1):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        numbers[x] = k
print(*numbers)
