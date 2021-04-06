a = int(input("Введите целое число от 1-12: \n"))
if a == 1 or a == 2 or a == 12:
    print("Зима\n")
elif a == 3 or a == 4 or a == 5:
    print("Весна\n")
elif a == 6 or a == 7 or a == 8:
    print("Лето\n")
elif a == 9 or a == 10 or a == 11:
    print("Осень\n")
else:
    print('Вы ввели неправильное число\n')
