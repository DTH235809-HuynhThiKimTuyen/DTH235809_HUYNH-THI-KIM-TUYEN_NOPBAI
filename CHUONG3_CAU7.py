
import datetime

while True:
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        
        # Tạo đối tượng ngày (sẽ báo lỗi nếu nhập sai)
        d = datetime.date(nam, thang, ngay)
        break  # Nếu không lỗi thì thoát vòng lặp
    except ValueError:
        print("Ngày tháng năm không hợp lệ, vui lòng nhập lại!\n")

# Cộng thêm 1 ngày
ngay_ke_tiep = d + datetime.timedelta(days=1)

print("Ngày kế tiếp là: {}/{}/{}".format(
    ngay_ke_tiep.day, ngay_ke_tiep.month, ngay_ke_tiep.year))

