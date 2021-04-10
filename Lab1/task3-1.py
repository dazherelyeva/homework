import random
n = int(input("Введите размер списка: \n"))
A = []
for i in range(n):# индекс из заданного списка
    a = random.randint(0, 100)  #рандомно выбирает из промежутка
    A.append(a)  #добавляет число в список
print(A)
s = int(input("Введите элемент: \n"))
for i in range(n):
    if i == s:
        r = A[s] #число из массива
        A.remove(r)
        print(A)
