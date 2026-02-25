S = input("Введите строку").lower().split()
words = {}
for i in S:
    words[i] = words.get(i, 0) + 1

for i in words:
    print(i, words[i])


