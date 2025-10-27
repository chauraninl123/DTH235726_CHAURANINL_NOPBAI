from random import randrange

lst = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    lst.append(randrange(0, 100))
print("List sau khi tạo ngẫu nhiên là:")
print(lst)

x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

k = int(input("Mời nhập số để xóa: "))
while k in lst:
    lst.remove(k)
print("List sau khi xóa:")
print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

if CheckDoiXung(lst):
    print("List đối xứng")
else:
    print("List không đối xứng")
