import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

result = math.sqrt(a + math.sqrt(b + math.sqrt(c)))
print("Kết quả căn bậc 2 lồng nhau =", round(result, 4))
