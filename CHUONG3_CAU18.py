
# save as draw_shapes.py and run: python draw_shapes.py
def shape1_square_border(n):
   
    if n <= 0:
        return
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print('* ' * n)
        else:
            if n == 1:
                print('*')
            else:
                print('* ' + '  ' * (n - 2) + '*')

def shape2_right_triangle_border(n):
    
    # hàng i (1..n), cột j (1..n)
    if n <= 0:
        return
    for i in range(1, n + 1):
        line = []
        for j in range(1, n + 1):
            # in '*' khi:
            # - cột đầu (j == 1) => tạo cạnh trái thẳng
            # - trên đường chéo từ (1,1) đến (n,n): j == i
            # - hàng cuối => in đầy (cạnh đáy)
            if j == 1 or j == i or i == n:
                line.append('*')
            else:
                line.append(' ')
        # thêm dấu cách giữa các cột để khoảng cách đều
        print(' '.join(line))

def shape3_toprow_leftcol_diagonal(n):
   
    if n <= 0:
        return
    for i in range(1, n + 1):
        line = []
        for j in range(1, n + 1):
            # in '*' khi:
            # - hàng đầu (i == 1)
            # - cột trái (j == 1)
            # - đường chéo đi từ (1,n) xuống (n,1) hay từ (1,1) xuống (n,n)?
            # Ở đây ta dùng đường chéo từ trái trên xuống phải dưới: j == i
            if i == 1 or j == 1 or j == i:
                line.append('*')
            else:
                line.append(' ')
        print(' '.join(line))


if __name__ == "__main__":
    try:
        n = int(input("Nhập n (chiều cao, số nguyên dương): ").strip())
    except Exception:
        print("Giá trị nhập không hợp lệ. Mặc định n = 6")
        n = 6

    print("\nHình 1: Hình vuông rỗng (kích thước n):")
    shape1_square_border(n)

    print("\nHình 2: Tam giác vuông (biên trái + đường chéo + đáy):")
    shape2_right_triangle_border(n)

    print("\nHình 3: Hàng đầu đầy + cột trái + đường chéo (phiên bản mẫu):")
    shape3_toprow_leftcol_diagonal(n)

