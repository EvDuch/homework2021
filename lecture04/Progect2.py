from random import randint
N = int(input())
arraychik = []
for i in range(N):
 arraychik.append(randint(-9999999999, 9999999999))

print("неотсортированный список:", arraychik)

for i in range(N-1):
 for j in range(N-i-1):
  if arraychik[j] > arraychik[j+1]:
   arraychik[j], arraychik[j+1] = arraychik[j+1], arraychik[j]

print("отсортированный список:", arraychik)