
# Xuất bảng cửu chương 2 -> 9

for i in range(1, 11):        # vòng lặp cho số nhân (1 -> 10)
    for j in range(2, 10):    # vòng lặp cho số bảng (2 -> 9)
        print(f"{j} * {i} = {j*i:<4}", end="\t")
    print()  # xuống dòng sau mỗi hàng
