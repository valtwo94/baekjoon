N, M = map(int, input().split())
baskets = []

for i in range(0, N):
    baskets.append(i + 1)
for _ in range(0, M):
    i, j = map(int, input().split())
    reversed_baskets = baskets[i-1:j][::-1]
    baskets[i-1:j] = reversed_baskets

print(*baskets)