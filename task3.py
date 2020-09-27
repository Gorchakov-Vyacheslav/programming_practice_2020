#3.Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
lst = input().split(' ')
k = 0
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[j] == lst[i]):
            k+=1
print(k)