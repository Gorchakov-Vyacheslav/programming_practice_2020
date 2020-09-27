#Выведите все элементы списка с четными индексами (то есть lst[0], lst[2], lst[4], ...).
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])