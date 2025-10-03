'''
-Các loại lỗi phổ biến:
SyntaxError: Lỗi cú pháp.
NameError: Biến chưa khai báo.
TypeError: Sai kiểu dữ liệu.
ValueError: Giá trị không hợp lệ.
ZeroDivisionError: Chia cho 0.
IndexError: Truy cập ngoài phạm vi danh sách.
KeError: Truy cập key không tồn tại trong dict.
-Cách bắt lỗi dùng cấu trúc try-except:
try:
    a = int(input("Nhập số: "))
    b = 10 / a
except ZeroDivisionError:
    print("Lỗi: Chia cho 0")
except ValueError:
    print("Lỗi: Phải nhập số")
except Exception as e:
    print("Lỗi khác:", e)
else:
    print("Kết quả:", b)
finally:
    print("Kết thúc")
    '''