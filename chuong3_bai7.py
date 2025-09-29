def ngay_ke_tiep(d, m, y):
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        ngay_trong_thang[1] = 29
    d += 1
    if d > ngay_trong_thang[m-1]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y

d, m, y = map(int, input("Nhập ngày/tháng/năm: ").split("/"))
d, m, y = ngay_ke_tiep(d, m, y)
print(f"Ngày kế tiếp: {d}/{m}/{y}")
