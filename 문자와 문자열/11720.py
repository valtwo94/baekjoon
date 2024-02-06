N = int(input())
word = str(input())
word_length = len(word)
sum = 0
for i in range(0, word_length):
    number = int(word[i])
    sum += number
print(sum)