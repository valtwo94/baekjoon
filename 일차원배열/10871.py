N, X = map(int, input().split())
numbers = list(map(int, input().split()))
result = [num for num in numbers if num < X]
print(*result)