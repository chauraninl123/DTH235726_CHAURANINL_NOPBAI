from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

def LayDong(D, r):
    return D[r]

def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val

m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
D = TaoMaTran(m, n)
print("Ma trận ngẫu nhiên:")
XuatMaTran(D)

r = int(input("Nhập dòng muốn xuất: "))
print("Dòng", r, ":")
XuatList1Chieu(LayDong(D, r))

c = int(input("Nhập cột muốn xuất: "))
print("Cột", c, ":")
XuatList1Chieu(LayCot(D, c))

print("Giá trị lớn nhất trong ma trận =", MAX(D))
