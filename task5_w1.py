#По данному натуральном n вычислите сумму 1! + 2! + 3! + ... + n!. В решении этой задачи можно использовать только один цикл.
n = int(input())
k = 1
sum = 0
for i in range(1,n + 1):
    k *= i
    sum = sum + k

print(sum)