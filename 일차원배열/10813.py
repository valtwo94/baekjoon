N, M = map(int, input().split())
numbers = []
str = ""
for i in range(0, N):
    numbers.append(i + 1)
for _ in range(0, M):
    i, j = map(int, input().split())
    x = numbers[i - 1]
    y = numbers[j - 1]
    numbers[i - 1] = y
    numbers[j - 1] = x
print(*numbers)
