class Customer:
    def __init__(self, i, l, n, s, a, c, b):
        self.id = i
        self.lastname = l
        self.name = n
        self.surname = s
        self.address = a
        self.card_number = c
        self.balance = b

    def __repr__(self):
        return '({}, {}, {}, {}, {}, {}, {})'.format(self.id, self.lastname, self.name, self.surname, self.address, self.card_number, self. balance)

    def get_card_number(self):
        return self.card_number

cust1 = Customer(1000, 'Ожерельев', 'Александр', 'Сергеевич', 'Жировичи', 1235, 7000)
cust2 = Customer(3040, 'Жуковская', 'Анна', 'Сергеевна', 'Клецк', 4567, 3000)
cust3 = Customer(2342, 'Кот', 'Олег', 'Иванович', 'Слоним', 2222, 1000)
cust4 = Customer(6723, 'Анищик', 'Петр', 'Николаевич', 'Минск', 8001, 54)
cust5 = Customer(4533, 'Хролович', 'Ольга', 'Иосифовна', 'Ганцевичи', 5495, 6000)

customers = [cust1, cust2, cust3, cust4, cust5]

from operator import attrgetter
sorted_customers = sorted(customers, key=attrgetter('lastname'))
#sorted_customers = sorted(customers, key=lambda e: e.lastname)

for argument in sorted_customers:
    print(argument)

a = int(input('Введите интервал от: \n'))
b = int(input('Введите интервал до: \n'))

for i in range(len(customers)):
    if a <= customers[i].get_card_number() <= b:
        print(customers[i])