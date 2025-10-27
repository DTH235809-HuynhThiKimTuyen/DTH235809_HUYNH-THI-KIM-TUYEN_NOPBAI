def HamXuLyChuoi():
    print("===== CÁC HÀM QUAN TRỌNG TRONG XỬ LÝ CHUỖI PYTHON =====\n")

    print("1. Nhóm hàm chuyển đổi:")
    print(" - s.upper()    : Chuyển chuỗi thành chữ IN HOA")
    print(" - s.lower()    : Chuyển chuỗi thành chữ in thường")
    print(" - s.title()    : Viết hoa chữ cái đầu mỗi từ")
    print(" - s.capitalize(): Viết hoa chữ cái đầu tiên của chuỗi\n")

    print("2. Nhóm hàm xóa hoặc cắt khoảng trắng:")
    print(" - s.strip()  : Xóa khoảng trắng ở đầu và cuối chuỗi")
    print(" - s.lstrip() : Xóa khoảng trắng bên trái")
    print(" - s.rstrip() : Xóa khoảng trắng bên phải\n")

    print("3. Nhóm hàm cắt và ghép chuỗi:")
    print(" - s.split(sep)       : Cắt chuỗi thành danh sách theo ký tự phân cách")
    print(" - 'sep'.join(list)   : Ghép danh sách thành chuỗi")
    print(" - s.replace(a, b)    : Thay thế chuỗi a bằng b\n")

    print("4. Nhóm hàm tìm kiếm và đếm:")
    print(" - s.find(sub)  : Trả về vị trí đầu tiên của chuỗi con")
    print(" - s.rfind(sub) : Tìm từ phải qua trái")
    print(" - s.count(sub) : Đếm số lần xuất hiện chuỗi con")
    print(" - sub in s     : Kiểm tra chuỗi con có trong chuỗi gốc không\n")

    print("5. Nhóm hàm kiểm tra:")
    print(" - s.isalpha() : Kiểm tra có phải toàn chữ cái không")
    print(" - s.isdigit() : Kiểm tra có phải toàn chữ số không")
    print(" - s.islower() : Kiểm tra có phải toàn chữ thường không")
    print(" - s.isupper() : Kiểm tra có phải toàn chữ hoa không")
    print(" - s.isspace() : Kiểm tra có phải toàn khoảng trắng không\n")

    print("6. Các hàm tiện ích khác:")
    print(" - len(s)             : Độ dài chuỗi")
    print(" - s.startswith(x)    : Kiểm tra chuỗi bắt đầu bằng x")
    print(" - s.endswith(x)      : Kiểm tra chuỗi kết thúc bằng x")
    print("==========================================================")

# Gọi hàm để in thông tin
HamXuLyChuoi()
