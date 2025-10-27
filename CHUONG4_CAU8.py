import math

a = float(input("Nhập cơ số a: "))
x = float(input("Nhập giá trị x: "))

if a > 0 and a != 1 and x > 0:
    logax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {round(logax, 4)}")
else:
    print("Giá trị không hợp lệ! (a > 0, a ≠ 1, x > 0)")
