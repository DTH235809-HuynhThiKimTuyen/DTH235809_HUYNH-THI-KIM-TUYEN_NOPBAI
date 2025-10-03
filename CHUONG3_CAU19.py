
# S(x,n) = x + x^2/(2+1) + x^3/(3+1) + ... + x^n/(n+1)

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(1, n+1):
    S += x**i / (i + 1)

print("Giá trị S(x,n) =", S)

