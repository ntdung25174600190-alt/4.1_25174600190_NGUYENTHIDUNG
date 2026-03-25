chu_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}
n = input("Nhập số: ")
ket_qua = ""
for i in range(len(n)):
    ket_qua += chu_so[n[i]]
    if i < len(n) - 1: 
        ket_qua += " "
print(ket_qua)