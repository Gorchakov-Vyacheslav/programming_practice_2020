#4.Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
lst = input().split(' ')
k = 0
for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if ((j!=i)&(lst[j] == lst[i])):
            break
    else:
        print(lst[i], end = " ")