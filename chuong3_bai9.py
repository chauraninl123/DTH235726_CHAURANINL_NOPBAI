m = int(input("Nhập tháng: "))
if 1 <= m <= 3:
    print("Quý 1")
elif 4 <= m <= 6:
    print("Quý 2")
elif 7 <= m <= 9:
    print("Quý 3")
elif 10 <= m <= 12:
    print("Quý 4")
else:
    print("Tháng không hợp lệ")
