#BONUS.
dict = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        #увеличиваем счетчик для конкретного слова на 1
        dict[word] = dict.get(word,0) + 1
print(dict)
