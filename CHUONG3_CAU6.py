def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    if n < 10:  # số có 1 chữ số
        return don_vi[n] if n > 0 else "không"
    
    chuc = n // 10
    dv = n % 10
    
    # đọc phần chục
    if chuc == 1:
        ket_qua = "mười"
    else:
        ket_qua = don_vi[chuc] + " mươi"
    
    # đọc phần đơn vị
    if dv == 0:
        return ket_qua
    elif dv == 1 and chuc > 1:
        return ket_qua + " mốt"
    elif dv == 5 and chuc > 0:
        return ket_qua + " lăm"
    else:
        return ket_qua + " " + don_vi[dv]


# ---- chương trình chính ----
n = int(input("Nhập số n (0-99): "))
print("n=>", doc_so(n))



