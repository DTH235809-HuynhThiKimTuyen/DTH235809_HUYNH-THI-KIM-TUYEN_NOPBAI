def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_hoan_thien(n):
    return tong_uoc(n) == n

def la_thinh_vuong(n):
    return tong_uoc(n) > n


# --- Chương trình chính ---
n = int(input("Nhập một số nguyên dương: "))

if la_hoan_thien(n):
    print(f"{n} là số hoàn thiện ✅")
elif la_thinh_vuong(n):
    print(f"{n} là số thịnh vượng 💰")
else:
    print(f"{n} không phải số hoàn thiện cũng không phải số thịnh vượng ❌")
