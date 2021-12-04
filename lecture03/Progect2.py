import math
a = input()
b = input()
try:
 a = int(a)
 b = int(b)
except:
 print("некорректный ввод")
 exit()
if (a < 1 or b < 1):
 print("некорректный ввод")
 exit()
print(math.gcd(a, b))