N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for i in range(0, N):
    scores[i] = scores[i] / M * 100
print(sum(scores)/len(scores))
