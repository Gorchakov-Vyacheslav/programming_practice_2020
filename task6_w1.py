#Последовательность состоит из различных натуральных чисел и завершается числом 0.
# Определите значение второго по величине элемента в этой последовательности.
# Гарантируется, что в последовательности есть хотя бы два элемента.
first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)
