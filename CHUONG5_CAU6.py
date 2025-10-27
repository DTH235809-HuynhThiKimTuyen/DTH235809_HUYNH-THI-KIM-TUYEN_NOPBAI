import re

def NegativeNumberInStrings(s):
    negatives = re.findall(r'-\d+', s)
    if negatives:
        print("Các số nguyên âm trong chuỗi là:", ', '.join(negatives))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# --- Chạy chương trình ---
chuoi = input("Nhập chuỗi bất kỳ: ")
NegativeNumberInStrings(chuoi)
