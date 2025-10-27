import os

def LayTenFile(duongdan):
    # Lấy tên file có phần mở rộng
    ten_file = os.path.basename(duongdan)
    return ten_file

def LayTenBaiHat(duongdan):
    # Lấy tên file không có phần mở rộng
    ten_bai_hat = os.path.splitext(os.path.basename(duongdan))[0]
    return ten_bai_hat

# Ví dụ:
duong_dan = r"d:\music\muabui.mp3"
print("Tên file:", LayTenFile(duong_dan))
print("Tên bài hát:", LayTenBaiHat(duong_dan))
