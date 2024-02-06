word = str(input())
dial = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
seconds = 0
for i in range(0, len(word)):
    for j in range(0, len(dial)):
        if word[i] in dial[j]:
            seconds += j + 2
print(seconds)
