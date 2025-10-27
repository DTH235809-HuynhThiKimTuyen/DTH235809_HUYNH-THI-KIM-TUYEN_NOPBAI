def ToiUuChuoi(s):
    words = s.strip().split()
    optimized = ' '.join(word.capitalize() for word in words)
    return optimized

# --- Chạy chương trình ---
chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu là:", ToiUuChuoi(chuoi))
