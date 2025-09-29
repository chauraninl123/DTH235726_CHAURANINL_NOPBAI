n = int(input("Nhập chiều cao n: "))

print("Chọn hình cần vẽ:")
print("1. Hình vuông rỗng")
print("2. Tam giác vuông")
print("3. Tam giác vuông ngược")

choice = int(input("Nhập lựa chọn (1-3): "))

if choice == 1:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

elif choice == 2:
    for i in range(1, n+1):
        print("* " * i)

elif choice == 3:
    for i in range(n, 0, -1):
        print("* " * i)

else:
    print("Lựa chọn không hợp lệ!")
