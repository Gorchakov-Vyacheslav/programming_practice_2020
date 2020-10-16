N = int(input())
M = int(input())
mtrx = [[int(input()) for i in range(N)] for j in range(M)]
def sum_diag():
    sum = 0
    sum_back = 0
    for i in range(N):
        for j in range(M):
            if (i == j):
                sum += mtrx[i][j]
            if (j == N-i-1):
                sum_back += mtrx[i][j]
    return [sum,sum_back]

choice =(input("Главная или побочная: "))
if (choice == 'главная'):
    print(sum_diag())
if (choice == 'побочная'):
    print(sum_diag())
