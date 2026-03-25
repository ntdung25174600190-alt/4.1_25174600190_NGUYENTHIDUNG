while True:
    n = int(input("Nhập số > 100: "))
    if n > 100:
        break
tong = 0
for i in str(n):
    tong += int(i)
print("Tổng chữ số =", tong)