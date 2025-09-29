def doc_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 0 or n > 99:
        return "Chỉ hỗ trợ số có tối đa 2 chữ số (0 - 99)."
    if n < 10:
        return chu_so[n]
    chuc = n // 10
    donvi = n % 10
    if donvi == 0:
        return chu_so[chuc] + " mươi" if chuc > 1 else "mười"
    if chuc == 1:
        if donvi == 5:
            return "mười lăm"
        else:
            return "mười " + chu_so[donvi]
    if donvi == 1:
        return chu_so[chuc] + " mươi mốt"
    elif donvi == 5:
        return chu_so[chuc] + " mươi lăm"
    else:
        return chu_so[chuc] + " mươi " + chu_so[donvi]

nums = [5, 10, 15, 21, 35, 40, 99]
for n in nums:
    print(n, "=>", doc_so(n))
