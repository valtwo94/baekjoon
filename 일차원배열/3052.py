numbers = []
for i in range(0, 10):
    x = int(input()) % 42
    if x not in numbers:
        numbers.append(x)
print(len(numbers))
