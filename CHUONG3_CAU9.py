1
# Vòng lặp nhập tháng hợp lệ
while True:
    thang = int(input("Nhập tháng (1-12): "))
    if 1 <= thang <= 12:
        break
    else:
        print("Tháng không hợp lệ, vui lòng nhập lại!\n")

# Xác định quý
if 1 <= thang <= 3:
    print("Tháng", thang, "thuộc Quý 1")
elif 4 <= thang <= 6:
    print("Tháng", thang, "thuộc Quý 2")
elif 7 <= thang <= 9:
    print("Tháng", thang, "thuộc Quý 3")
else:  # 10-12
    print("Tháng", thang, "thuộc Quý 4")
