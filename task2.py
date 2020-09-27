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