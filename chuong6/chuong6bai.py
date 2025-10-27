from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))
lst = [randrange(-100, 100) for _ in range(n)]
print("List ngẫu nhiên là:")
print(lst)

value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm:")
print(lst)

k = int(input("Bạn muốn đếm số nào: "))
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng =", tongnt)

lst.sort()
print("List sau khi sắp xếp:")
print(lst)

del lst
try:
    print(lst)
except:
    print("List đã bị xóa.")
