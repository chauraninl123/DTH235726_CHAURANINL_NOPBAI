print(""" Trình bày một số cách nhập dữ liệu từ bàn phím: 
Cách nhập	           Cú pháp ví dụ                    	         Ghi chú
Nhập chuỗi	            name = input()	                              Luôn trả về kiểu str
Nhập số nguyên	        age = int(input())	                          Dùng int() để ép kiểu
Nhập số thực	        x = float(input())	                          Dùng float() để ép kiểu
Nhập nhiều giá trị  	a, b = input().split()	                      Trả về chuỗi, cần ép kiểu nếu cần
Nhập danh sách số	    lst = list(map(int, input().split()))	      Dùng map() và list() """)