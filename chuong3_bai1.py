print("Truong trinh kiem tra nam nhuan")
year=int(input("Moi Thim nhap vao mot nam:"))
if (year %4==0 and year % 100 != 0) or year % 400 == 0 :
    print ("Nam",year ," la nam nam nhuan")
else:
        print("Nam",year,"khong nhuan")