import math


ABside = float(input("Введите пожалуйста длину стороны AB: "))
ACside = float(input("Введите пожалуйста длину стороны AC: "))
corner = float(input("Введите пожалуйста градус угла нашего треугольника: "))
print(math.sqrt(ABside**2+ACside**2-2*ACside*ABside*(math.cos(math.radians(corner))))) 
