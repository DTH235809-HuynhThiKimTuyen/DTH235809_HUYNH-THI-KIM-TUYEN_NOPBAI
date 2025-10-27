# Câu 11
def sum1(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

def sum2(n):
    global val
    s = 0
    while n > 0:
        s += val
        val -= 1
    return s

def sum3(n):
    s = 0
    for i in range(n, 0, -1):
        s += i
    return s


# ===== Trường hợp 1 =====
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum2(5))
    print(sum3(5))

print("Trường hợp 1:")
main()


# ===== Trường hợp 2 =====
def main2():
    global val
    val = 10
    print(sum1(5))
    print(sum2(5))
    print(sum3(5))

print("\nTrường hợp 2:")
main2()


# ===== Trường hợp 3 =====
def main3():
    global val
    val = 5
    print(sum2(5))
    print(sum2(5))
    print(sum3(5))

print("\nTrường hợp 3:")
main3()
