import math

ABside = int(input("Введите пожалуйста длину стороны AB: "))
ACside = int(input("Введите пожалуйста длину стороны AC: "))
corner = math.cos(int(input("Введите пожалуйста градус Цельсия угла нашего треугольника: ")))
print(round(ABside**+ACside**-2*ACside*ABside*(math.cos(corner*180 / math.pi))))