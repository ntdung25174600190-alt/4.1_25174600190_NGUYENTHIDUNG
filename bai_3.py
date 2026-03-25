while True:
    x = float(input("Nhập số: "))
    if x < 0 or x != int(x):
        print("Dừng chương trình")
        break
    print("Số hợp lệ:", int(x))