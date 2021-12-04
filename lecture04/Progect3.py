import random
N = int(input())
arraychik = random.sample(range(-9999999999, 9999999999), N)
print("неотсортирован:", arraychik)
def sorted(arraychik):
 for i in range(0, len(arraychik)-1):
  if (arraychik[i] > arraychik[i + 1]):
   return False
 return True
def meshaem(arraychik):
 random.shuffle(arraychik)
def bogosort(arraychik):
 while(not(sorted(arraychik))):
  meshaem(arraychik)
bogosort(arraychik)
print("отсортирован:", arraychik)