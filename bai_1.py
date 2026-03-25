while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
S1 =0
for i in range(1, n + 1):
    S1 += i ** 2
S2 = 0
for i in range(n + 1):
    S2 += (2 * i + 1) ** 3
S3 = 0
for i in range(1, n + 1):
    S3 += (2 * i) ** 4
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i - 1)) / i
S5 = 0
for i in range(1, n + 1):
    S5 += 1 / (i * (i + 1))
import math
S6 = 0
for i in range(2, n + 1):
    S6 += 1 / math.sqrt(i)

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)