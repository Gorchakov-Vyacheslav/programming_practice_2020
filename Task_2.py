#1.Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей.
a = input().split(' ')
k = 0
for i in range(1, len(a)-1):
    if ((a[i] > a[i-1])&(a[i] > a[i+1])) :
        k+=1
print(k)

#2.В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка
lst = list(map(int, input()))
max = min = lst[0]
j = k = 0
for i in range(1, len(lst)):
    if (lst[i]>max):
        max = lst[i]
        j = i
    if (lst[i]<min):
        min = lst[i]
        k = i
max = lst[j]
lst[j] = lst[k]
lst[k] = max
print(lst)

#3.Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
lst = input().split(' ')
k = 0
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[j] == lst[i]):
            k+=1
print(k)

#4.Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
lst = input().split(' ')
k = 0
for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if ((j!=i)&(lst[j] == lst[i])):
            break
    else:
        print(lst[i], end = " ")

#5.Даны два списка чисел.Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания
print(*sorted(set(input().split(' ')) & set(input().split(' ')), key =int))

#6.Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
lst = input().split(' ')
k = 0
for i in range(0,len(lst)):
    for j in range(0,i):
        if ((j != i)&(lst[j] == lst[i])):
            print("YES")
            break
    else:
        print("NO")

#7.Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
words = set()
n = int(input())

for i in range(n):
    words.update(input().split())
print(len(words))

#8.Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#Для слова из словаря, записанного в последней строке, определите его синоним.
n = int(input())
dict = {}

for i in range(n):
    first,second = input().split()
    dict[first] = second
    dict[second] = first
print(dict[input()])

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

#BONUS.
#Дан текст. Для каждого слова в тексте посчитать сколько раз оно встречается.
dict = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        #увеличиваем счетчик для конкретного слова на 1
        dict[word] = dict.get(word,0) + 1
print(dict)
