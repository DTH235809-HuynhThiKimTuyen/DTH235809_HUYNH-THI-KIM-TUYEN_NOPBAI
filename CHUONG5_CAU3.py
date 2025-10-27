def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(abs(x) ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# Cho phép nhập chuỗi từ bàn phím
s = input("Nhập chuỗi số (cách nhau bằng dấu chấm phẩy ';'): ")

arr = s.split(';')
sochan = 0
soam = 0
sont = 0
tong = 0

print("\nCác số trong chuỗi:")
for x in arr:
    print(x)
    number = int(x)
    # Đếm số chẵn
    if number % 2 == 0:
        sochan += 1
    # Đếm số âm
    if number < 0:
        soam += 1
    # Đếm số nguyên tố
    if CheckPrime(number):
        sont += 1
    # Cộng tổng để tính trung bình
    tong += number

# Xuất kết quả
print("\nSố chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
