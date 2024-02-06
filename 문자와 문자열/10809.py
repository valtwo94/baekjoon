import string
S = str(input())
alphabets = string.ascii_lowercase
numbers = []
for i in range(0, len(alphabets)):
    if alphabets[i] in S:
        numbers.append(S.index(alphabets[i]))
    else:
        numbers.append(-1)
print(*numbers)