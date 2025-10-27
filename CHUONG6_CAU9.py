
# --- Nhập mảng số tự nhiên ---
M = []
n = int(input("Nhập số phần tử của mảng: "))

for i in range(n):
    x = int(input(f"Nhập M[{i}]: "))
    while x < 0:
        print("❌ Vui lòng nhập số tự nhiên (>= 0)!")
        x = int(input(f"Nhập lại M[{i}]: "))
    M.append(x)

print("\nMảng bạn vừa nhập là:", M)

# --- Hàm kiểm tra số nguyên tố ---
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Dòng 1: Số lẻ ---
odd = [x for x in M if x % 2 != 0]
print("\nDòng 1 - Các số lẻ:", odd, f"→ Tổng cộng {len(odd)} số lẻ")

# --- Dòng 2: Số chẵn ---
even = [x for x in M if x % 2 == 0]
print("Dòng 2 - Các số chẵn:", even, f"→ Tổng cộng {len(even)} số chẵn")

# --- Dòng 3: Số nguyên tố ---
prime = [x for x in M if CheckPrime(x)]
print("Dòng 3 - Các số nguyên tố:", prime)

# --- Dòng 4: Không phải số nguyên tố ---
not_prime = [x for x in M if not CheckPrime(x)]
print("Dòng 4 - Các số không phải nguyên tố:", not_prime)
