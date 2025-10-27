def oscillate(a, b):
    # Từ a đến b, mỗi lần i tăng 1
    for i in range(a, b):
        yield i
        yield -i

# Kiểm tra kết quả
for n in oscillate(-3, 5):
    print(n, end=' ')
