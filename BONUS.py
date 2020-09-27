#9.Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего.
#Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
dict = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        #увеличиваем счетчик для конкретного слова на 1
        dict[word] = dict.get(word,0) + 1
max_val = max(dict.values())
top_words = [k for k, v in dict.items() if v == max_val] #все слова, которые встречались max_val раз
print(min(top_words))
