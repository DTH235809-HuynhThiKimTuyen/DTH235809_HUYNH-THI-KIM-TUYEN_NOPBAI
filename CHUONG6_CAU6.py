from random import sample

n = int(input("Nhập số phần tử N: "))
# sample(range(...), n) tạo list ngẫu nhiên KHÔNG trùng
lst = sample(range(0, 100), n)

print("List ngẫu nhiên không trùng nhau là:")
print(lst)
