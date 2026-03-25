while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    else:
        print("Mẫu phải khác 0, nhập lại!")

print("Phân số là:", tu_so, "/", mau_so)
print("Giá trị =", tu_so / mau_so)