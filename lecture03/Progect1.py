N = input()
try:
 N = int(N)
except:
 print("введите число")
 exit()
if (N < 2):
 print("введите корректное число")
arraychikB = set(range(2, N+1))
while arraychikB:
 prime = min(arraychikB)
 print(prime, end = "\t")
 arraychikB -= set(range(prime, N+1, prime))