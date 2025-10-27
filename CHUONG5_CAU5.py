def DemKyTu(s):
    nguyen_am = "aeiouAEIOU"
    in_hoa = in_thuong = chu_so = dac_biet = khoang_trang = nguyenam = phuam = 0

    for ch in s:
        if ch.isupper():
            in_hoa += 1
        elif ch.islower():
            in_thuong += 1
        elif ch.isdigit():
            chu_so += 1
        elif ch.isspace():
            khoang_trang += 1
        else:
            dac_biet += 1

        # Kiểm tra nguyên âm / phụ âm
        if ch.isalpha():
            if ch in nguyen_am:
                nguyenam += 1
            else:
                phuam += 1

    print("Số chữ IN HOA:", in_hoa)
    print("Số chữ in thường:", in_thuong)
    print("Số chữ số:", chu_so)
    print("Số ký tự đặc biệt:", dac_biet)
    print("Số khoảng trắng:", khoang_trang)
    print("Số nguyên âm:", nguyenam)
    print("Số phụ âm:", phuam)


# Chương trình chính
s = input("Nhập vào 1 chuỗi bất kỳ: ")
DemKyTu(s)
