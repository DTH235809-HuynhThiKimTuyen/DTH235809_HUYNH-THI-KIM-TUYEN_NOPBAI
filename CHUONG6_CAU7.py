

n = int(input("Nhập số phần tử: "))
lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i}: "))
        # Nếu không phải phần tử đầu tiên, kiểm tra tăng dần
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print("❌ Sai quy tắc tăng! Vui lòng nhập lại (phải > phần tử trước).")

print("Dãy số tăng dần hợp lệ là:")
print(lst)
