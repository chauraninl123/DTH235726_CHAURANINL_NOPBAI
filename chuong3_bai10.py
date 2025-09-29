x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = x

for i in range(2, n + 1):
    tu = x ** i
    mau = 1
    for j in range(1, i + 1):
        mau *= j
    s += tu / mau

print("S({}, {}) = {}".format(x, n, s))
