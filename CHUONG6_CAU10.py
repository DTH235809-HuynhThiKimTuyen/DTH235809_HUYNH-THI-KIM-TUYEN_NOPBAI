print("=== CÂU 10: XỬ LÝ MA TRẬN ===")

# --- Hàm nhập ma trận ---
def NhapMaTran(ten):
    m = int(input(f"Nhập số dòng của ma trận {ten}: "))
    n = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}] = "))
            row.append(x)
        M.append(row)
    return M

# --- Hàm xuất ma trận ---
def XuatMaTran(M):
    for row in M:
        for element in row:
            print(f"{element:8.2f}", end="")
        print()
    print()

# --- Hàm cộng hai ma trận ---
def CongMaTran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# --- Hàm hoán vị ma trận ---
def HoanVi(M):
    # zip(*M) hoán đổi dòng ↔ cột
    transposed = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return transposed


# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================

# Nhập 2 ma trận
A = NhapMaTran("A")
B = NhapMaTran("B")

print("\nMa trận A:")
XuatMaTran(A)
print("Ma trận B:")
XuatMaTran(B)

# Kiểm tra kích thước để cộng
if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = CongMaTran(A, B)
    print("Ma trận C = A + B là:")
    XuatMaTran(C)
else:
    print("❌ Hai ma trận không cùng kích thước, không thể cộng!")

# --- Hoán vị ---
print("Ma trận hoán vị của A là:")
XuatMaTran(HoanVi(A))

print("Ma trận hoán vị của B là:")
XuatMaTran(HoanVi(B))
