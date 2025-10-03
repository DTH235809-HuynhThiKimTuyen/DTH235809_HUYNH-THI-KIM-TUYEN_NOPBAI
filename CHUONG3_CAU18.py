
n = int(inp4
        ut("Nhập chiều cao n: "))

print("Hình 1:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nHình 2:")
for i in range(1, n+1):
    print("* " * i)

print("\nHình 3:")
for i in range(n, 0, -1):
    print("  " * (n-i) + "* " * i)

print("\nHình 4:")
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)

