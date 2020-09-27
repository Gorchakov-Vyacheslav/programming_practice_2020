#8.Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#Для слова из словаря, записанного в последней строке, определите его синоним.
n = int(input())
dict = {}

for i in range(n):
    first,second = input().split()
    dict[first] = second
    dict[second] = first
print(dict[input()])