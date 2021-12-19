class Operation:  #Задаём базовые операции над числами

    def plus(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def umnoj(self, x, y):
        print(x * y)

    def delenie(self, x, y):
        print(x / y)

    def modul(self, x, y):
        print(abs(7 + 8j))

    def stepen(self, x, y):
        print(pow(x + y, 2))


obj1 = Operation()   #Задаем значения x и y
x = complex(5, 6)
y = complex(7, 8)

obj1.plus(x, y)

obj1.minus(x, y)

obj1.umnoj(x, y)

obj1.modul(x, y)

obj1.delenie(x, y)

obj1.stepen(x, y)

class ComplexNumber:   #Основной цикл
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Где сумма c1 и c2 равна:')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Где произведение c1 и c2 равно:')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(1, -2)

c_2 = ComplexNumber(3, 4)

print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)