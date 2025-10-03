
# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if op == '+':
    ketqua = a + b
elif op == '-':
    ketqua = a - b
elif op == '*':
    ketqua = a * b
elif op == '/':
    if b != 0:
        ketqua = a / b
    else:
        ketqua = "Lỗi: không thể chia cho 0"
else:
    ketqua = "Phép toán không hợp lệ!"

# Xuất kết quả
print("Kết quả:", ketqua)

