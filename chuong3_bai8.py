a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == "+":
    kq = a + b
elif op == "-":
    kq = a - b
elif op == "*":
    kq = a * b
elif op == "/":
    if b != 0:
        kq = a / b
    else:
        kq = "Không thể chia cho 0"
else:
    kq = "Phép toán không hợp lệ"

print("Kết quả:", kq)
