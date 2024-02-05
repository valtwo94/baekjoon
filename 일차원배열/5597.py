numbers = []
for i in range(1, 29):
    numbers.append(int(input()))
for i in range(1, 31):
    if numbers.count(i) == 0:
        print(i)